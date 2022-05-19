from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    price=serializers.DecimalField(decimal_places=2,max_digits=6)


    def create(self, validated_data):
        service=Service()
        service.title=validated_data.get('title')
        service.description=validated_data.get('description')
        service.price=validated_data.get('price')
        service.save()
        return service

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price=validated_data.get('price',instance.price)
        return instance


 