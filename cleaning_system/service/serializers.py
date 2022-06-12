from rest_framework import serializers
from  .models  import Service
from   company.models  import Company
from django.http import Http404
class  ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

    def create(self, validated_data):
        company=self.get_company(self.context.get("company_id"))
        return  Service.objects.create(**validated_data, company=company)

    def get_company(self,company_id):
        try:
           return Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            raise Http404
