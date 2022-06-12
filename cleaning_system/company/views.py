
from django.views import View

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpRequest, JsonResponse
from django.http import Http404

from  .models  import Company,  Rating
from  .serializers  import CompanySerializer,  RatingSerializer
from  rest_framework.permissions  import  IsAuthenticated
class  CompanyViewSet(viewsets.ViewSet):
    permission_classes=[IsAuthenticated]
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404
    def retrieve(self, request, pk=None):
        company=self.get_object(pk)
        serializer=CompanySerializer(instance=company,  context={'user':request.user})
        return Response(serializer.data)

    def create(self, request):
        data=JSONParser().parse(request)
        serializer=CompanySerializer(data=data, context={'owner':request.user})
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def update(self, request, pk=None):
        company=self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        company=self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       
class  RatingViewSet(viewsets.ViewSet):
    def  create(self,request,  **kwargs):
        data=JSONParser().parse(request)
        data.update()
        serializer=RatingSerializer(data=data, context={'user':request.user,'company':self.kwargs["company_id"]})
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
    def update(self,request, **kwargs):
        try:
            company=Company.objects.get(pk=self.kwargs['company_id'])
            rating=Rating.objects.get(company=company,  user=request.user)
        except  Rating.DoesNotExist:
            raise  Http404
        serializer = RatingSerializer(rating, data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


   
