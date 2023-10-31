from django.urls import path
from . import views

urlpatterns = [
    path('imobiliaria', views.imobiliaria, name='imobiliaria'),
]