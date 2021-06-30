from django.contrib import admin
from django.urls import path, include
from .views import index,coraje,doraemon,garfield,gatos,patan,perros,scooby,tom

urlpatterns = [
    path('',index,name='INDEX'),
    path('perros/coraje/',coraje,name='CORAJE'),
    path('gatos/doraemon/',doraemon,name='DORAEMOS'),
    path('gatos/garfield/',garfield,name='GARFIELD'),
    path('gatos/',gatos,name='GATOS'),
    path('perros/patan/',patan,name='PATAN'),
    path('perros/',perros,name='PERROS'),
    path('perros/scooby/',scooby,name='SCOOBY'),
    path('gatos/tom/',tom,name='TOM'),

]
