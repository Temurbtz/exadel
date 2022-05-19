from rest_framework import serializers
from  .models  import Company
from service_type.models import Service


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        depth=1


   

class  CompanyCreateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Company
        fields = '__all__'

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
 