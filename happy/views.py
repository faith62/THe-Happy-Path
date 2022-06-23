from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import  Counselor
from .serializers import CounselorSerializer
from rest_framework.decorators import api_view

#Counselor
class CounselorList(APIView):
    def get(self, request, format=None):
        all_counselor = Counselor.objects.all()
        serializers = CounselorSerializer(all_counselor, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = CounselorSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def showcounselor(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        counselor = Counselor.objects.get(id=pk)
    except counselor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CounselorSerializer(counselor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CounselorSerializer(counselor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        counselor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)















