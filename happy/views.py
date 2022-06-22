from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import  Service
from .serializers import ServiceSerializers
from rest_framework.decorators import api_view

#service 
class ServiceList(APIView):
    def get(self, request, format=None):
        all_service = Service.objects.all()
        serializers = ServiceSerializers(all_service, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ServiceSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)   

@api_view(['GET', 'PUT', 'DELETE'])
def showservice(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        service = Service.objects.get(id=pk)
    except service.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ServiceSerializers(service)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServiceSerializers(service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 

