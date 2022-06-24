from rest_framework import serializers
from user.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        max_length=128, min_length=6, write_only=True)
    class Meta:
        model=User
        fields=('username', 'email', 'password',)

        def create(self,validated_data):
            return User.objects.create_user(validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        max_length=128, min_length=6, write_only=True)
    class Meta:
        model=User
        fields=('token', 'email', 'password',)
        
    read_only_fields =['token']
    