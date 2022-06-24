from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny 
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token

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
            token = Token.objects.get_or_create(user=account)[0].key

            data['message'] = "user registered successfully"
            data['email'] = account.email
            data['username'] = account.username
            data["token"] = token 
        else:
            data = serializer.errors
    return Response(data)

'''
Login view.
Verify that the user is in the database
'''
@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    if request.method == 'POST':
        data = {}
        reqData = LoginSerializer(data=request.data.dict())
        print(reqData)
        if reqData.is_valid():
            name =reqData.__getitem__('username')
            pass_word =reqData.__getitem__('password')
            username = name.value
            password = pass_word.value
            print(password)
            try:
                user = User.objects.get(username=username)
                print(user)
            except BaseException as e:
                raise ValidationError({"message": "Bad Request"})

            if not check_password(password, user.password):
                raise ValidationError({"message": "Incorrect Login credentials"})

            if user:
                if user.is_active:
                    login(request, user)
                    data["message"] = "user logged in"
                    data["email_address"] = user.email

                    response = {"data": data}

                    return Response(response)
                else:
                    raise ValidationError({"message": "Account not active"})
            else:
                raise ValidationError({"message": "Account doesnt exist"})