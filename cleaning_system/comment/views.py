
from  .serializers  import CommentSerializer
from  .models import Comment
from  company.models  import Company

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpRequest, JsonResponse
from django.http import Http404


class  CommentViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
    def list(self, request, company_id):
        data=Company.objects.get(pk=company_id).comment_set
        serializer = CommentSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    def update(self, request, pk=None):
        comment=self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        comment=self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
      
