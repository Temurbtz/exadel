
from django.http import JsonResponse
from django.http import Http404
from  .serializers import  CompanySerializer, CompanyCreateSerializer
from  .models  import Company
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status


class CompanyViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404
    def list(self, request):
        companies=Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        data=JSONParser().parse(request)
        postserializer=CompanyCreateSerializer(data=data)
        if  postserializer.is_valid():
            company=postserializer.save()
            getserializer=CompanySerializer(company)
            return JsonResponse(getserializer.data, status=201)
        return JsonResponse(postserializer.errors, status=400)

    def retrieve(self, request, pk=None):
        company=self.get_object(pk)
        serializer=CompanySerializer(company)
        return Response(serializer.data)

    def update(self, request, pk=None):
        company=self.get_object(pk)
        updateserializer = CompanyCreateSerializer(company, data=request.data)
        if  updateserializer.is_valid():
            company=updateserializer.save()
            getserializer=CompanySerializer(company)
            return JsonResponse(getserializer.data, status=201)
        return JsonResponse(updateserializer.errors, status=400)

    def destroy(self, request, pk=None):
        company=self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



