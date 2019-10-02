from django.urls import path
from . import views 

#Create a view here

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]