from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from  .models  import Request
from .serializers   import RequestSerializer


class RequestList(APIView):
    def get(self, request, format=None):
        requestt = Request.objects.all()
        serializer = RequestSerializer(requestt, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestDetail(APIView):
    def get_object(self, pk):
        try:
            return Request.objects.get(pk=pk)
        except Request.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        requestt = self.get_object(pk)
        serializer = RequestSerializer(requestt)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        requestt= self.get_object(pk)
        serializer = RequestSerializer(requestt, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        requestt = self.get_object(pk)
        requestt.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
