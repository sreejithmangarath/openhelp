from django.contrib import admin
from app import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index),
    path('registerseller',views.RegisterSeller,name='registerseller'),
    path('registeruser',views.RegisterUser,name='registeruser'),
    path('login',views.Login,name='login'),
    path('userhome',views.userhome,name='userhome'),
    path('sellerhome',views.sellerhome,name='sellerhome'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('ProductsList',views.ProductsList,name='productslist'),

    
   ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)