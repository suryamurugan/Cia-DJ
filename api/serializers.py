from rest_framework.serializers import ModelSerializer
from rest_auth.registration.serializers import RegisterSerializer

from .models import User
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ( 'email', 'username', 'password','usn','dept','user_t')
        #fields = '__all__'
    def create(self, validated_data):
        user = User(**validated_data)
       # user.__setattr__('is_staff',True)
        # Hash the user's password.
        user.set_password(  ['password'])
        user.save()
        return user

class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    name = serializers.CharField(required=True)
    usn = serializers.CharField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
                'password1': self.validated_data.get('password1', ''),
                'email': self.validated_data.get('email', ''),
                'name': self.validated_data.get('name', ''),
                'usn' : self.validated_data.get('usn',''),
               
        }