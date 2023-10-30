from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

from django.conf.urls.static import static

from . import views 


urlpatterns = [ 
    path("", views.index, name="index"),
    path("adm/", views.propriedades, name= "propriedades"),
    path("detalheadm/", views.detalhespropriedades, name= "detalhespropriedades"),
    
    
]