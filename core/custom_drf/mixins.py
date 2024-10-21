from rest_framework import status
from rest_framework.mixins import (CreateModelMixin as drf_CreateModelMixin,
                                   ListModelMixin as drf_ListModelMixin,
                                   RetrieveModelMixin as drf_RetrieveModelMixin,
                                   UpdateModelMixin as drf_UpdateModelMixin,
                                   DestroyModelMixin as drf_DestroyModelMixin)
from rest_framework.response import Response


class CreateModelMixin(drf_CreateModelMixin):
    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_request_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)

        response_serializer = self.get_response_serializer(instance)
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListModelMixin(drf_ListModelMixin):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            response_serializer = self.get_response_serializer(page, many=True)
            return self.get_paginated_response(response_serializer.data)

        serializer = self.get_response_serializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveModelMixin(drf_RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_response_serializer(instance)
        return Response(serializer.data)


class UpdateModelMixin(drf_UpdateModelMixin):
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_request_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        response_serializer = self.get_response_serializer(data=serializer.data)
        response_serializer.is_valid(raise_exception=True)
        return Response(response_serializer.data)


class DestroyModelMixin(drf_DestroyModelMixin):
    pass
