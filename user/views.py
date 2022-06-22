from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from rest_framework.decorators import permission_classes, api_view
from .models import ClientProfile
from .serializers import *

# Create your views here.

class ClientProfileList(generics.ListCreateAPIView):
    '''Display all client profiles as json data'''
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer

class ClientProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    '''Display client profile as json data by id provided'''
    queryset = ClientProfile.objects.all()
    serializer_class = ClientProfileSerializer

'''
Registration test for API endpoints
Returns email and username as JSon data   
'''
@api_view(["POST"])
@permission_classes([AllowAny])
def user_registration(request):
    if request.method == 'POST':
        data = {}
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            account.is_active = True
            # Set user a client
            account.is_client = True
            account.save()

            data['message'] = "user registered successfully"
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
    return Response(data)