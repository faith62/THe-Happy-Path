from rest_framework.serializers import ModelSerializer
from .models import Contact



class ContactSerializer(ModelSerializer):

    class Meta:
        model=Contact
        field='__all__'