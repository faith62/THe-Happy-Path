from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import  Service
from .serializers import ServiceSerializers

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
# Create your views here.
