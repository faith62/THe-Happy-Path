from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import User,ClientProfile

class ClientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientProfile
        fields = ('user', 'prof_pic', 'about_me', 'full_name')

class RegistrationSerializer(serializers.ModelSerializer):
    '''Serializers registration requests and creates a new user.'''
    # Setup confirm password validation field
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ('username','email','password','password2')
        extra_kwargs = {'password':{'write_only':True}}

    def save(self):
        new_user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'Passwords must match'})
        new_user.set_password(password)
        new_user.save()
        return new_user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(style={'input_type':'text'})
    password = serializers.CharField(style={'input_type':'password'})

    class Meta:
        model = User
        fields = ('username','password')

class UpdateClientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientProfile
        fields = ('about_me', 'full_name','prof_pic')

    def update(self, instance, validated_data):
        instance.about_me = validated_data['about_me']
        instance.full_name = validated_data['full_name']

        instance.save()

        return instance