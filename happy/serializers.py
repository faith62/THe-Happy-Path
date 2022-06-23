from rest_framework import serializers
from .models import Contact
from .models import Service

class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('__all__')

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contact
        fields='__all__'

