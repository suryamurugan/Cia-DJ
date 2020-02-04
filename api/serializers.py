from rest_framework.serializers import ModelSerializer
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from allauth.account import app_settings as allauth_settings
from allauth.utils import (email_address_exists, get_username_max_length)
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from phonenumber_field.modelfields import PhoneNumberField

from .models import User,Events,UserType,UserTypeRegister,News,AttendRegister,Project,InterestGroup,InterestGroupMember
from rest_framework import serializers
from cia import settings
from django.contrib.auth import get_user_model, authenticate


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

class visioneerSerializer(ModelSerializer):
    class Meta:
        fields='__all__'

class UserSerializer2(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ( 'email', 'username', 'password','usn','dept','user_t')
        #fields = '__all__'
'''   def create(self, validated_data):
        user = User(**validated_data)
       # user.__setattr__('is_staff',True)
        # Hash the user's password.
        user.set_password(  ['password'])
        user.save()
        return user'''
''' def save(self, validated_data):
        user = User(**validated_data)
       # user.__setattr__('is_staff',True)
        # Hash the user's password.
        user.set_password(  ['password'])
        user.save()
        return user
'''

'''
class CustomRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)
    usn = serializers.CharField(required=True)
    
    

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
                'password1': self.validated_data.get('password1', ''),
                'email': self.validated_data.get('email', ''),
                'username': self.validated_data.get('username', ''),
                'usn' : self.validated_data.get('usn',''),
               
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.address = self.cleaned_data.get('usn')
#user.user_type = self.cleaned_data.get('user_type')
        user.save()
        return user
'''

class InterestGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestGroup
        fields = ("id", "g_name","g_desc","g_img","g_head",'g_tellink','g_medium')
""" class InterestGroupMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestGroupMember
        fields = ("user") """

class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','username','usn')
        read_only_fields = ('email',)

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ("e_id","e_state","e_title","e_date",'e_start_time','e_end_time','e_venue','e_organizer','e_description','e_score','e_registration_link','e_photos_link','e_medium_link')
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("n_id","n_title","n_desc","n_author","n_datetime",'n_image','n_link')
class AttendRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendRegister
        fields = ("arid","e_id","u_id","a_datetime")

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



class UserTypeSerializer(serializers.ModelSerializer):
   # ut_id = serializers.SerializerMethodField()
    #def get_id(self, obj):
     #  return getattr(obj, 'ut_id', 1)
    class Meta:
        model = UserType()
        fields = ('ut_id','ut_name')





#using this for user type id  to be validated
class RegisterSerializerCustom(serializers.Serializer):
    
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    usn = serializers.CharField(required=True)
    user_t = serializers.IntegerField(write_only=True)
    #user_type = PrimaryKeyRelatedField()
   

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        '''if data['password'] != data['password'] :
            raise serializers.ValidationError(_("The two password fields didn't match."))\
        #checking here for user type 
        if data['ut_type'] == 0:
            raise serializers.ValidationError(_("You cannot register as superuser"))'''
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
            
            
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user



# THIS FOR SURE WORKS BRO
class UserSerializerMain(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'email', 'username', 'password','usn','dept','user_t')
        write_only_fields = ('password',)
       # read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            usn = validated_data['usn'],
            
            #first_name=validated_data['first_name'],
            #last_name=validated_data['last_name']

        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password': self.validated_data.get('password', ''),
            'email': self.validated_data.get('email', ''),
            'usn': self.validated_data.get('usn', ''),
        }
            
    def save(self, request):
        adapter = get_adapter()
        print(request)
        user = adapter.new_user(request)
        print(user.username)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)

        setup_user_email(request, user, [])
        return user


class NewRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    usn = serializers.CharField(required=True)
    dept = serializers.IntegerField(required=True)
    ut_id = serializers.IntegerField(required=True)
    phone_number = serializers.CharField(required=True)
    
   # user_t = serializers.IntegerField(write_only=True)
    #user_type = PrimaryKeyRelatedField()
  #  email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
   # first_name = serializers.CharField(required=True, write_only=True)
    #last_name = serializers.CharField(required=True, write_only=True)
    #address = serializers.CharField(required=True, write_only=True)
    #password1 = serializers.CharField(required=True, write_only=True)
    #password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                _("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            #'last_name': self.validated_data.get('last_name', ''),
            #'address': self.validated_data.get('address', ''),
            #'user_type': self.validated_data.get('user_type', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'usn': self.validated_data.get('usn', ''),
            'phone_number': self.validated_data.get('phone_number', ''),
            'ut_id': self.validated_data.get('ut_id', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        user.is_active = False
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])

        #user.address = self.cleaned_data.get('usn')

        #user.user_type = self.cleaned_data.get('user_type')

        user.save()
        return user


### THIS IS A CUSTOM LOGIN SERIALIZER
class CustomLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})
    phone = serializers.CharField(required=False, allow_blank=True)

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username(self, username, password):
        user = None

        if username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username_email(self, username, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        elif username and password:
            user = self.authenticate(username=username, password=password)
        else:
            msg = _('Must include either "username" or "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')

        user = None

        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings

            # Authentication through email
            if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.EMAIL:
                user = self._validate_email(email, password)

            # Authentication through username
            elif app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:
                user = self._validate_username(username, password)

            # Authentication through either username or email
            else:
                user = self._validate_username_email(username, email, password)

        else:
            # Authentication without using allauth
            if email:
                try:
                    username = UserModel.objects.get(email__iexact=email).get_username()
                except UserModel.DoesNotExist:
                    pass

            if username:
                user = self._validate_username_email(username, '', password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # If required, is the email verified?
        if 'rest_auth.registration' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                email_address = user.emailaddress_set.get(email=user.email)
                if not email_address.verified:
                    raise serializers.ValidationError(_('E-mail is not verified.'))
        print(user)
        attrs['user'] = user
        return attrs

