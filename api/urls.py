from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from .views import CreateUserView,UserCreateAPIView,CustomRegisterView,ListEventsView,ListNewsView,attend,getstats,ProjectView,LoginUserDetailView,CustomLoginView,VeryNewCustomRegisterView,activate,testReset,ListInterestGroupView
from allauth.account.views import confirm_email
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView

from rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView
from .views import something,getmembers
from django.contrib.auth.views import password_reset_confirm,password_reset_complete



urlpatterns = [
  path('attend/', attend), # FOR ATTENDANCE
  path('getstats/',getstats), # FOR GETTING STATS
  path('getProjects/',ProjectView.as_view()), # GET PROJECTS 
  path('events/', ListEventsView.as_view(), name='getevents'),  # <-- And here
  path('news/', ListNewsView.as_view(), name='getnews'),  # <-- And here
   path('interestgroup/', ListInterestGroupView.as_view(), name='getinterestgroup'),  # <-- And here
  path('rest-auth/', include('rest_auth.urls')), # ALL REST AUTH URLS
  path('getmembers/', getmembers), # FOR ATTENDANCE

  
  ]