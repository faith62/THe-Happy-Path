from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Service
from .serializers import ServiceSerializers

#service 
class ServiceList(APIView):
    def get(self, request, format=None):
        all_service = Service.objects.all()
        serializers = ServiceSerializers(all_service, many=True)
        return Response(serializers.data)
# Create your views here.
