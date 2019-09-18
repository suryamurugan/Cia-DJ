from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from .views import CreateUserView,UserCreateAPIView,CustomRegisterView,ListEventsView
from allauth.account.views import confirm_email
from django.contrib import admin


urlpatterns = [
   # path('events/', ListEventsView.as_view(), name="events-all"),
   # path('news/', ListNewsView.as_view(), name="news-all"),
   # path('users/', UserListView.as_view(), name="events-all"),
    path('users/', CustomRegisterView.as_view(),name="something"),  #DJANGO USER
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')), #REST USER
    #path('rest-auth/registration/account-confirm-email', CustomRegisterView.as_view()), #REST USER
    path('admin/',admin.site.urls, name='account_confirm_email'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('events/', ListEventsView.as_view(), name='getevents'),  # <-- And here
   # path('auth/', CustomRegisterView.as_view(), name="auth-all"),
]