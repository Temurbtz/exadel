
from rest_framework.decorators import api_view
from .models import Notification
from django.http import Http404
from django.http import  JsonResponse
@api_view(['PUT'])
def update_status(request, pk=None):
     if request.method == 'PUT':
         try:
            notification=Notification.objects.get(pk=pk)
         except:
            raise Http404

         notification.status=1
         notification.save()
         return JsonResponse(request.data,status=201)

