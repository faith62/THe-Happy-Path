from django.shortcuts import render
from rest_framework import generics
from .models import ClientProfile
from .serializers import ClientProfileSerializer

# Create your views here.

class ClientProfileList(generics.ListCreateAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer

class ClientProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer