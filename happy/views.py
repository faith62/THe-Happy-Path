from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .serializers import ContactSerializer
from .models import Contact


class contactList(APIView):
    def get(self,request, format=None):
        queryset = Contact.objects.all()
        serializer=ContactSerializer(queryset,many=True)
   
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(): #if all values are correct 
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, pk):
    """
    Retrieve, update or delete a code contact.
    """
    try:
       Contact= Contact.objects.get(id=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =ContactSerializer(Contact)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(Contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)