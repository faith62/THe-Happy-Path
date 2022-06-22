from rest_framework import serializers

from .models import Counselor


class CounselorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counselor
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')