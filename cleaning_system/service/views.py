

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse
from django.http import Http404

from  .models  import Service
from .serializers  import ServiceSerializer
class ServiceViewSet(viewsets.ViewSet):
    def   get_service(self,service_id):
        try:
           return Service.objects.get(pk=service_id)
        except Service.DoesNotExist:
            raise Http404

    def create(self, request, **kwargs):
        data=JSONParser().parse(request)
        serializer=ServiceSerializer(data=data, context={'company_id': self.kwargs['company_id']})
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    def retrieve(self, request, **kwargs):
        service=self.get_service(self.kwargs['service_id'])
        serializer=ServiceSerializer(service)
        return Response(serializer.data)

    def update(self, request, **kwargs):
        service=self.get_service(self.kwargs['service_id'])
        serializer = ServiceSerializer(service, data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def destroy(self, request, **kwargs):
        service=self.get_service(self.kwargs['service_id'])
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


    

