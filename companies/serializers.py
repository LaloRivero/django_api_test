''' Companies models serializers '''

# Django REST Framework
from rest_framework import serializers


class CompanyModelSerializer(serializers.Serializer):
    ''' Handels Company Data '''

    name = serializers.CharField(min_length=8, max_length=50)
    description = serializers.CharField(min_length=20, max_lenght=100)
    ticker = serializers.CharField(min_length=4, max_length=5)
    values = serializers.CharField(min_length=100, max_length=250)

    def validate(self, data):
        ''' Verify that the values are an integer number
            and there are 50 of them. '''

        values = int(data['values'].split(','))
        cont=0
        for num in values:
            if type(num) != int:
                raise serializers.ValidationError({'Error':'Not a valid input'})
            cont+=1

        if cont != 50:
            raise serializers.ValidationError({'Error':'You need to enter a 50 integer values'})