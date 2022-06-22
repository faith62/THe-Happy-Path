from urllib import request
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . models import Contact
# Create your views here.

class ContactList(ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
        