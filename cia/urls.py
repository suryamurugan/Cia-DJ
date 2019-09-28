"""cia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path, include
from django.conf.urls import url

from allauth.account.views import confirm_email
from api.views import attend,something,getUser

from api.views import HelloView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sarath/<something>/',something),
    path('getUser/',getUser),
    path('hello/', HelloView.as_view(), name='hello'),
   # url(r'^api/v1/rest-auth/registration/account-confirm-email/(?P<key>[-/\w]+)/$', confirm_email, name='account_confirm_email'), 

    re_path('api/(?P<version>(v1|v2))/', include('api.urls')),
    #url(r'rest-auth/registration/ ^account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),name='account_confirm_email'),
    


]
