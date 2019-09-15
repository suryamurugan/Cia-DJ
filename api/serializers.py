from rest_framework.serializers import ModelSerializer
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