from django.contrib import admin
from app import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index),
    #path('empregister',views.empregister),
    
   ]