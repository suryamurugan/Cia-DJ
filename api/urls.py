from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from .views import CreateUserView,UserCreateAPIView,CustomRegisterView,ListEventsView,ListNewsView,attend,getstats,ProjectView,LoginUserDetailView,CustomLoginView,VeryNewCustomRegisterView,activate,testReset
from allauth.account.views import confirm_email
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView

from rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from django.contrib.auth.views import password_reset_confirm



urlpatterns = [
  path('attend/', attend), # FOR ATTENDANCE
  path('getstats/',getstats), # FOR GETTING STATS
  path('getProjects/',ProjectView.as_view()), # GET PROJECTS 
  path('users/', CustomRegisterView.as_view(),name="something"),  #DJANGO USER
  path('rest-auth/', include('rest_auth.urls')), # ALL REST AUTH URLS
  url(r'rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),name='account_confirm_email'),
  path('rest-auth/registration/', include('rest_auth.registration.urls')), #REST USER
  path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
  path('events/', ListEventsView.as_view(), name='getevents'),  # <-- And here
  path('news/', ListNewsView.as_view(), name='getnews'),  # <-- And here
  url(r'^login/$', LoginUserDetailView.as_view(), name='rest_login'),
  url(r'^custom/login/$', CustomLoginView.as_view(), name='rest_login'),
  url(r'^custom/register/$', VeryNewCustomRegisterView.as_view(), name='rest_register'),
  path(r'^*account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(), name='account_confirm_email'),  # <-- And here
  ]