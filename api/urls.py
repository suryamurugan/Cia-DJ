from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from .views import CreateUserView,UserCreateAPIView,CustomRegisterView,ListEventsView,ListNewsView,attend
from allauth.account.views import confirm_email
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView

from rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView



urlpatterns = [
   # path('events/', ListEventsView.as_view(), name="events-all"),
   # path('news/', ListNewsView.as_view(), name="news-all"),
   # path('users/', UserListView.as_view(), name="events-all"),
  path('attend/', attend), # FOR ATTENDANCE
   path('users/', CustomRegisterView.as_view(),name="something"),  #DJANGO USER
   path('rest-auth/', include('rest_auth.urls')),
  # url(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
  #      name='account_confirm_email'),
   url(r'rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),name='account_confirm_email'),
   path('rest-auth/registration/', include('rest_auth.registration.urls')), #REST USER
  # path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),name='account_confirm_email'), #REST USER
  
   # path('admin/',admin.site.urls, name='account_confirm_email'),
   path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
   path('events/', ListEventsView.as_view(), name='getevents'),  # <-- And here
   path('news/', ListNewsView.as_view(), name='getnews'),  # <-- And here
   # path('auth/', CustomRegisterView.as_view(), name="auth-all"),
   #url(r'^', include('django.contrib.auth.urls')),


 #  path(r'^*account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(), name='account_confirm_email'),  # <-- And here
#   url(r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
    ##    name='account_confirm_email'),
]