from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,EventsSerializer,NewsSerializer,AttendRegisterSerializer,ProjectSerializer
from rest_framework.permissions import AllowAny
from rest_auth.registration.views import RegisterView
from .models import User,Events,News,AttendRegister,Project
from . import serializers
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework import status
from rest_framework.authtoken.models import Token




#from rest_framework import serializers

class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

'''SEND POST REQUEST WITH BODY : {token: <TOKEN>,e_code: <EVENT_CODE>}'''
@api_view(['GET'])
def something(request,something ):
    return Response({"response":something})

'''SEND POST REQUEST WITH BODY : {token: <TOKEN>,e_code: <EVENT_CODE>}'''
@api_view(['POST'])
def getUser(request):
    print(request.data)
    #token = Token.objects.get(key=request.data['token'])
    return Response({"response"})

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

class ListNewsView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class ProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


'''SEND POST REQUEST WITH BODY : {token: <TOKEN>,e_code: <EVENT_CODE>}'''
@api_view(['POST'])
def attend(request,version):
    if request.method == 'POST':
        print(request.body)
        try:
            token = Token.objects.get(key=request.data['token'])
            event = Events.objects.get(e_code=request.data['e_code'])
            print(event)
            print(token.user)
            #attendregister = AttendRegister.objects.filter(e_id=event,u_id=token.user).count()  
            attendregister = AttendRegister.objects.filter(e_id=event,u_id=token.user).count()
            print('DINA:')
            print(attendregister)
        except:
            return Response({"response":False})
        '''try: 
            

            #total_count = AttendRegister.objects.filter(u_id=token.user).count()
            print('SSSS'.attendregister)
            #return Response({"response":False})
        except:
            return Response({"response":False})
            print('')'''
       # print(attendregister)
        
        print(event.e_score)
        print(token.user)
        if event.e_state:
            if attendregister == 0:
                serializer = AttendRegister(e_id=event,u_id=token.user)
                #if serializer.is_valid():
                serializer.save()
                #event = Events.objects.get()
                #attend_register = AttendRegister.
                #return Response({'token': token.key, 'id': token.user.username})
                return Response({'response':True})
        else: 
            return Response({'response':False})

'''SEND POST REQUEST WITH BODY : {token: <TOKEN>,e_code: <EVENT_CODE>}'''
@api_view(['POST'])
def getstats(request,version):
    if request.method == 'POST':
        print(request.body)
        try:
            token = Token.objects.get(key=request.data['token'])
            total_count = AttendRegister.objects.filter(u_id=token.user).count()
            allevents = AttendRegister.objects.filter(u_id=token.user)
            score_sum =0
            for i in allevents:
                score_sum=score_sum+i.e_id.e_score
            return Response({"response":True,"score_sum":score_sum,"total_count":total_count})
            #print(sum)
            #print('vndo'.AttendRegister.objects.filter(u_id=token.user))
            
            
        except:
            return Response({"response":False})
        return Response({"response":False})
       