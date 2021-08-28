from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    
   
    path('signup/', views.SignUp.as_view(), name='signup'),
   
]