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
        new_list = []
        for num in data.values:
            try:
                new_list.append(int(num))
            except:
                pass

        return new_list
