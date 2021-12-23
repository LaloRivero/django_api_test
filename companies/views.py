''' Company operations '''

# Django Rest Framework
from rest_framework import status, mixins, viewsets
from rest_framework.response import Response

# Models
from companies.models import Company

# Serializer
from companies.serializers import CompanySerializer


class CompanyViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def convert_str_to_list(self,data):
        ''' Convert an array of numbers save in the data base to a list as a response '''
        new_list = []
        for num in data.values:
            try:
                new_list.append(int(num))
            except:
                pass

        return new_list

    def list(self, request, *args, **kwargs):
        ''' List all the companies with pagination'''

        queryset = Company.objects.all()
        for q in queryset:
            q.values = self.convert_str_to_list(q)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        ''' Show a Company data '''

        instance = self.get_object()
        instance.values = self.convert_str_to_list(instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
