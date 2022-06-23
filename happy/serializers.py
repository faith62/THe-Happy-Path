from rest_framework import serializers
from .models import Contact
from .models import Service

class ServiceSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(source='contact.first_name')
    contact_last_name = serializers.CharField(source='contact.last_name')
    contact_phone_number = serializers.CharField(source='contact.phone_number')
    contact_email = serializers.CharField(source='contact.email')
    contact_location = serializers.CharField(source='contact.location')

    class Meta:
        model = Service
        fields = '__all__'
        

class ContactSerializer(serializers.ModelSerializer):
    # service = ServiceSerializers(source='service_set',many=True)
    class Meta:
        model=Contact
        fields='__all__'
        # fields=('service',)

