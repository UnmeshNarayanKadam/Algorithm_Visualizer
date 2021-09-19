from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('contact', views.contact, name='contact'),
    path('searchalgo', views.searchalgo, name='searchalgo'),
    path('sortalgo', views.sortalgo, name='sortalgo'),
    path('visualizer', views.visualizer, name='visualizer'),
    path('quize', views.quize, name='quize')
]
