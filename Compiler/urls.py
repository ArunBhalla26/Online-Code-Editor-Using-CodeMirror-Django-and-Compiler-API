
from django.urls import path 
from .views import *
urlpatterns = [
    
    path("", IndexView.as_view(), name="home"),
    path("compile/", compile_code, name='compile_code'),
]

