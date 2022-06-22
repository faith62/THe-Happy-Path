from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CounselorSerializer
from .models import Counselor
from rest_framework import status
from rest_framework.generics import GenericAPIView


# Create your views here.


class CounselorList(GenericAPIView):
    serializer_class = CounselorSerializer

    def get(self, request):
        counselors = Counselor.objects.all()
        serializer = CounselorSerializer(counselors, many=True)
        return Response(serializer.data)


class CounselorDetail(APIView):
    def get_object(self, pk):
        try:
            return Counselor.objects.get(pk=pk)
        except Counselor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        counselor = self.get_object(pk)
        serializer = CounselorSerializer(counselor)
        return Response(serializer.data)

    def put(self, request, pk):
        counselor = self.get_object(pk)
        serializer = CounselorSerializer(counselor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        counselor = self.get_object(pk)
        counselor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

