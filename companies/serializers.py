''' Companies models serializers '''

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from companies.models import Company

class CompanySerializer(serializers.Serializer):
    ''' Handels Company Data '''

    id = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    name = serializers.CharField(min_length=8, max_length=50)
    description = serializers.CharField(min_length=20, max_length=100)
    ticker = serializers.CharField(min_length=4,
                                   max_length=5,
                                   validators=[UniqueValidator(queryset=Company.objects.all())])
    values = serializers.ListField(child=serializers.IntegerField(min_value=0, max_value=100))

    def validate(self, data):
        ''' Verify that the values are an integer number
            and there are 50 of them. '''

        if len(data["values"]) != 50:
             raise serializers.ValidationError({'Error':'You need to enter a 50 integer values'})

        return data

    def create(self, data):
        ''' Handle the creation of a new company '''

        data["values"]=str(data["values"])
        company = Company.objects.create(name=data["name"],
                                         description=data["description"],
                                         ticker=data["ticker"],
                                         values=data["values"])
        return company

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)