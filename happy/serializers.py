from rest_framework import serializers
from .models import Contact
from .models import Service

from django.contrib.auth.models import User


class ServiceSerializers(serializers.ModelSerializer):   
    # contact_first_name = serializers.CharField(source='contact.first_name')
    # contact_last_name = serializers.CharField(source='contact.last_name')
    # contact_phone_number = serializers.CharField(source='contact.phone_number')
    # contact_email = serializers.CharField(source='contact.email')
    # contact_location = serializers.CharField(source='contact.location')
    
    class Meta:
        
        model = Service
        fields = '__all__'
        
        

class ContactSerializer(serializers.ModelSerializer):
    services = ServiceSerializers(many=True)

    def create(self, validated_data):
      services_data = validated_data.pop("services")
      contact = Contact.objects.create(validated_data)
      for service_data in services_data:
        Service.objects.create(contact=contact, service= service_data),
      return contact

    class Meta:
        model=Contact
        fields='__all__'
        # fields=('service',)


