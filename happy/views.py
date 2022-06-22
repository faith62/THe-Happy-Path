from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from user import serializers

from .serializers import ContactSerializer
from .models import Contact


class contactView(APIView):
    def get(self,request, *args, **kwargs):
        queryset = Contact.objects.all()
        serializer=ContactSerializer(queryset,many=True)
   
        return Response(serializer.data)


    def post(self,request,*args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(): #if all values are correct 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        