from rest_framework import serializers
from cleaning_company.models import Company
from   service_type.models  import Service
from .models  import Request
class RequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(),many=False)
    cleaning_type=serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=False)
    location=serializers.CharField(max_length=255)
    area=serializers.DecimalField(decimal_places=2,max_digits=6)
    hours=serializers.IntegerField()
    price=serializers.DecimalField(decimal_places=2,max_digits=6)

    

    def create(self, validated_data):
        request=Request()
        request.company=validated_data.get('company')
        request.cleaning_type=validated_data.get('cleaning_type')
        request.location=validated_data.get('location')
        request.area=validated_data.get('area')
        request.hours=validated_data.get('hours')
        request.price=validated_data.get('price')
        request.save()
        return request

    def update(self, instance, validated_data):
        instance.company=validated_data.get('company',instance.company)
        instance.cleaning_type=validated_data.get('cleaning_data',instance.cleaning_type)
        instance.location=validated_data.get('location',instance.location)
        instance.area=validated_data.get('area',instance.area)
        instance.hours=validated_data.get('hours',instance.hours)
        instance.price=validated_data.get('price',instance.price)
        return instance

 

 