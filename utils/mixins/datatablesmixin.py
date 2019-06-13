from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.views import View


class JQueryDataTablesMixin(View):
    http_method_names = ['post']

    def search_by_attributes(self, string, qs):
        result = []

        if len(string) == 0:
            return qs

        if len(qs) == 0:
            return result

        s = string.lower()

        if isinstance(qs, QuerySet):

            for row in qs:
                for attname in self.search_attributes:
                    if s in str(row.__getattribute__(attname)).lower():
                        result.append(row)
                        break
            return result

    def filter_queryset(self, qs):
        search = self.request.POST.get('search[value]', None)

        if search:
            qs = self.search_by_attributes(search, qs)
        return qs

    def order_queryset(self, qs):

        if len(qs) == 0:
            return qs
        # Order column
        order_field_idx = self.request.POST.get('order[0][column]', None)
        if order_field_idx:
            # Order priority
            order_dir = self.request.POST.get('order[0][dir]')
            # Order field
            order_field_name = self.request.POST.get('columns[%s][data]' %
                                                     order_field_idx)
            if isinstance(qs, QuerySet):
                attnames = [a.name for a in qs.model._meta.get_fields()]
                propnames = [p for p in qs.model._meta._property_names]
                if order_field_name in attnames:
                    if order_dir == 'desc':
                        qs = qs.order_by("-" + order_field_name)
                    elif order_dir == 'asc':
                        qs = qs.order_by(order_field_name)
                    else:
                        qs = qs.order_by('-created', order_field_name)
                elif order_field_name in propnames:

                    action = "sorted(qs, key=lambda t: t.{}, reverse=bool({}))".format(order_field_name, order_dir)

                    qs = eval(action)

            else:  # if its another iterable (prob from a mock)
                if order_field_name in qs[0].keys():
                    qs.sort(
                        key=lambda o: o[order_field_name],
                        reverse=bool(order_dir)
                    )
        return qs

    def get_page(self, request, *args, **kwargs):
        # handle pagination
        draw = int(request.POST.get('draw'))

        # Get queryset
        qs = self.get_queryset(**kwargs)
        total_count = len(qs)

        qs = self.order_queryset(qs)

        start, length = (int(request.POST.get('start')),
                         int(request.POST.get('length')))

        filtered_query = self.filter_queryset(qs)
        filtered_count = len(filtered_query)

        page = filtered_query[start:start + length]

        page = self.serialize_page(
            page,
            start=start,
            length=length,
            **kwargs
        )

        return JsonResponse(
            {
                'draw': draw,
                'data': page,
                'recordsTotal': total_count,
                'recordsFiltered': filtered_count,
            }
        )

    def post(self, request, *args, **kwargs):
        """
        Handle pagination of the list.
        """
        if request.is_ajax():  # datatable serverside processing
            return self.get_page(request, *args, **kwargs)

        response = JsonResponse({})
        response.status_code = 400
        return response


class PaginatorMixin(object):

    def get_queryset(self, *args, **kwargs):
        return []

    def serialize_page(self, page, *args, **kwargs):
        return []

    def get_page(self, start, length, *args, **kwargs):
        # Get queryset
        qs = self.get_queryset(**kwargs)
        total_count = len(qs)
        page = qs[start:start + length]

        page = self.serialize_page(page, **kwargs)

        return {
                'page': page,
                'recordsTotal': total_count,
                #'recordsFiltered': filtered_count,
            }