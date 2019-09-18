from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,EventsSerializer
from rest_framework.permissions import AllowAny
from rest_auth.registration.views import RegisterView
from .models import User,Events
from . import serializers

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class CustomRegisterView(RegisterView):
        queryset = User.objects.all()



class ListEventsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Events.objects.all()
    serializer_class = EventsSerializer