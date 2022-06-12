

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse
from django.http import Http404

from   .serializers  import RequestSerializer
from  .models  import  Request
class RequestViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Request.objects.get(pk=pk)
        except Request.DoesNotExist:
            raise Http404
    def create(self, request, **kwargs):
        data=JSONParser().parse(request)
        serializer=RequestSerializer(data=data, context={'company_id': self.kwargs['company_id'],'service_id':self.kwargs['service_id'],'user':request.user})
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def list(self, request):
        data=request.user.request_set
        serializer = RequestSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


    def destroy(self, request, request_id=None):
        data=self.get_object(request_id)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, request_id=None):
        request_object=self.get_object(request_id)
        serializer = RequestSerializer(request_object,request.data)
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


    

    

    


    

