from rest_framework import serializers

from  .models  import Request
from  company.models  import Company
from  service.models  import Service
from django.http import Http404
class  RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id','location','measurement_unit_count','total_cost']

    def create(self, validated_data):
        company=self.get_company(self.context.get("company_id"))
        service=self.get_service(self.context.get('service_id'))
        user=self.context.get('user')
        return  Request.objects.create(**validated_data, company=company, user=user, service=service)

    def get_company(self,company_id):
        try:
           return Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            raise Http404

    def get_service(self,service_id):
        try:
           return Service.objects.get(pk=service_id)
        except Service.DoesNotExist:
            raise Http404
