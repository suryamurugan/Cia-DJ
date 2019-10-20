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
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string


from rest_framework import status
from rest_framework.response import Response
from allauth.account import app_settings as allauth_settings
from allauth.account.utils import complete_signup
from rest_auth.views import LoginView
from rest_auth.registration.views import RegisterView
from rest_auth.app_settings import (
    TokenSerializer,  UserDetailsSerializer, JWTSerializer, create_token
)
from rest_auth.utils import jwt_encode


from cia import settings
from django.core.mail import EmailMessage




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

# CUSTOM LOGIN VIEW 
class LoginUserDetailView(LoginView):
    def get_response_serializer(self):
        if getattr(settings, 'REST_USE_JWT', False):
            response_serializer = JWTSerializer
        elif getattr(settings, 'REST_USE_TOKEN', True):
            response_serializer = TokenSerializer
        else:
            response_serializer = UserDetailsSerializer
        return response_serializer

    def login(self):
        self.user = self.serializer.validated_data['user']

        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(self.user)
        elif getattr(settings, 'REST_USE_TOKEN', True):
            self.token = create_token(self.token_model, self.user,
                                      self.serializer)

        if getattr(settings, 'REST_SESSION_LOGIN', True):
            self.process_login()

    def get_response(self):
        serializer_class = self.get_response_serializer()

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': self.user,
                'token': self.token
            }
            serializer = serializer_class(instance=data,
                                          context={'request': self.request})
        elif getattr(settings, 'REST_USE_TOKEN', True):
            serializer = serializer_class(instance=self.token,
                                          context={'request': self.request})
        else:
            serializer = serializer_class(instance=self.user,
                                          context={'request': self.request})

        return Response(serializer.data, status=status.HTTP_200_OK)

### NEXT CHECK - WORKING CUSTOM LOGIN - OVERRIDING get_response from LOGIN-VIEW
class CustomLoginView(LoginView):
    '''def get_response(self):
        orginal_response = super().get_response()
        print(orginal_response['key'])
        mydata = {"message": "some message", "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response'''
    def get_response(self):
        serializer_class = self.get_response_serializer()

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': self.user,
                'token': self.token
            }
            serializer = serializer_class(instance=data,
                                          context={'request': self.request})
        else:
            serializer = serializer_class(instance=self.token,
                                          context={'request': self.request})

        response = Response(serializer.data, status=status.HTTP_200_OK)
        if getattr(settings, 'REST_USE_JWT', False):
            from rest_framework_jwt.settings import api_settings as jwt_settings
            if jwt_settings.JWT_AUTH_COOKIE:
                from datetime import datetime
                expiration = (datetime.utcnow() + jwt_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(jwt_settings.JWT_AUTH_COOKIE,
                                    self.token,
                                    expires=expiration,
                                    httponly=True)
        #return response
        orginal_response = response
        #orginal_response = super().get_response()
        print(orginal_response)
        mydata = {"username": self.user.username,"email": self.user.email, "status": "success"}
        orginal_response.data.update(mydata)
        return orginal_response

## CUSTOM REGISTER VIEW

class VeryNewCustomRegisterView(RegisterView):
    def get_response_data(self, user):
        if allauth_settings.EMAIL_VERIFICATION == \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            return {"detail": _("Verification e-mail sent.")}

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': user,
                'token': self.token
            }
            return JWTSerializer(data).data
        else:
            #return TokenSerializer(user.auth_token).data
            orginal_response = TokenSerializer(user.auth_token).data
            print("ORIGINAL RESPONSE")
            print(orginal_response)
            #orginal_response = super().get_response()
            mydata = {"username": user.username,"email": user.email, "status": "success"}
            #current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user':user, 'domain':'current_site.domain',
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your CIA account.'
            to_email = user.email
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            print('MY DATA')
            print(mydata)
            orginal_response.update(mydata)
            print("ORIGINAL RESPONSE")
            print(orginal_response)
            return orginal_response



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

