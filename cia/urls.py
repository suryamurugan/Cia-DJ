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
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,re_path, include
from django.conf.urls import url

from allauth.account.views import confirm_email
from api.views import attend,something,getUser,activate,VeryNewCustomRegisterView,testReset,CustomLoginView,register,profile,VisioneerCreate,visioneerview,getjsonmodel,getjsonmodel2

from django.views.generic import TemplateView
from django.contrib.auth.views import password_reset_confirm,password_reset_complete

from api.views import HelloView,index,loginPage
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, RedirectView
from . import settings


urlpatterns = [

    path('getjsonmodel/',getjsonmodel,name="getjsonmodel"),
    path('getjsonmodel2/',getjsonmodel2,name="getjsonmodel2"),

    #FOR WEB
    path('admin/', admin.site.urls), # ADMIN url
   #url(r'^$', TemplateView.as_view(template_name="home.html"), name='hom   e'),
    path('accounts/',include('django.contrib.auth.urls')), # TO GET ALL USER URLS
    url(r'^account_inactive/$',TemplateView.as_view(),name = 'account_inactive'), # no idea y but register needs this
    path('',TemplateView.as_view(template_name="mainsite.html"),name="index"),
    path('events/',TemplateView.as_view(template_name="events.html"),name="events"),
    
    path('projects/',TemplateView.as_view(template_name="projects.html"),name="projects"),
    path('register/',register,name="register"),
    path('profile/',profile,name='profile'),
    path('visioneer/', visioneerview, name='visioneer'),
    
    
    re_path('api/(?P<version>(v1|v2))/', include('api.urls')),    

    #FOR MOBILE REST API's
    url(r'rest/register/$', VeryNewCustomRegisterView.as_view(), name='rest_register'),
    url(r'^rest/login/$', CustomLoginView.as_view(), name='main_login'),
    url(r'rest/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'), # POST RESET MAIL 
    url(r'rest/reset/confirm/done/$', password_reset_complete, name='password_reset_complete'),
    path('activate/<uid>/<token>/',something),     # ACTIVATEING ACCOUNT - LINK MAILED 
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

