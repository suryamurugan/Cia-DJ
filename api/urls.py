from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from .views import CreateUserView,UserCreateAPIView,CustomRegisterView,ListEventsView,ListNewsView,attend,getstats,ProjectView,LoginUserDetailView,CustomLoginView,VeryNewCustomRegisterView,activate
from allauth.account.views import confirm_email
from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView

from rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView



urlpatterns = [
   # path('events/', ListEventsView.as_view(), name="events-all"),
   # path('news/', ListNewsView.as_view(), name="news-all"),ImproperlyConfigured at /api/v2/rest-auth/user/

   # path('users/', UserListView.as_view(), name="events-all"),
  path('attend/', attend), # FOR ATTENDANCE
  path('getstats/',getstats),
   path('getProjects/',ProjectView.as_view()),
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

  # CUSTOM VIEW 
  url(r'^login/$', LoginUserDetailView.as_view(), name='rest_login'),
  url(r'^custom/login/$', CustomLoginView.as_view(), name='rest_login'),
  url(r'^custom/register/$', VeryNewCustomRegisterView.as_view(), name='rest_register'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
  #url(r'^signup/$', views.signup, name='signup'),
  #url(r'^account_inactive/$',TemplateView.as_view(),name = 'account_inactive'),
   path(r'^*account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(), name='account_confirm_email'),  # <-- And here
#   url(r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
    ##    name='account_confirm_email'),
]