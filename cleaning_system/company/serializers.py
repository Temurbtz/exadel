from dataclasses import fields
from django.http import Http404
from rest_framework import serializers
from  .models  import Company,  Rating
from  service.serializers  import  ServiceSerializer

class CompanySerializer(serializers.ModelSerializer):
    services=ServiceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Company
        fields = ['id','name','description','date_foundation','logo','services']
       

    def create(self, validated_data):
        company=Company()
        company.name=validated_data.get('name')
        company.description=validated_data.get('description')
        company.logo=validated_data.get('logo')
        company.owner=self.context.get('owner')
        company.save()
        return company
   
    

class  RatingSerializer(serializers.ModelSerializer):
    class  Meta:
        model=Rating
        fields=['rating']
    def  create(self,validated_data):
        try:
            company=Company.objects.get(pk=self.context.get('company'))
        except Company.DoesNotExist:
            raise Http404
        try:
            rating=Rating.objects.get(company=company,user=self.context.get('user'))
            return rating
        except :
           return Rating.objects.create(**validated_data,user=self.context.get('user'),company=company)

   
