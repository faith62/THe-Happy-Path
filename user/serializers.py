from rest_framework import serializers
from models import ClientProfile

class ClientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientProfile
        fields = ('user', 'prof_pic', 'about_me', 'full_name')