''' Companies models serializers '''

# Django REST Framework
from django.db.models import fields
from django.db.models.expressions import Value
from rest_framework import serializers

# Models
from companies.models import Company, Values


class ValuesModelSerializer (serializers.ModelSerializer):
    ''' Company model serializer'''

    class Meta:
        model = Values
        fields = ['value']


class CompanyModelSerializer(serializers.ModelSerializer):
    ''' Company Model Serializer '''

    values = ValuesModelSerializer()

    class Meta:
        model = Company
        fields = ['id','name','description','ticker', 'values']
        depth = 1