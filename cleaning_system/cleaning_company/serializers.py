from rest_framework import serializers
from  .models  import Company
from service_type.models import Service
import  datetime

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    description = serializers.CharField()
    operation_city = serializers.CharField(max_length=50)
    date_foundation=serializers.DateField(default=datetime.date.today())
    services=serializers.PrimaryKeyRelatedField(queryset=Service.objects.all(), many=True)


    def create(self, validated_data):
        company=Company()
        company.title=validated_data.get('title')
        company.description=validated_data.get('description')
        company.operation_city=validated_data.get('operation_city')
        company.save()
        company.services.set(validated_data.get('services'))
        return company

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.operation_city = validated_data.get('operation_city', instance.operation_city)
        instance.services.set(validated_data.get('services',instance.services))
        return instance


 