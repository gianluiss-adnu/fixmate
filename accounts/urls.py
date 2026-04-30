from django.urls import path
from . import views

urlpatterns = {
    # These are apparently functions for when users visits that url
    # THe functions below are subject to change... Initial setup

#    path('register/', views.register), 
    path('', views.overview, name='dashboard'),
    path('register/user', views.register_user),
    path('register/handyman', views.register_handyman),
    path('login/', views.login),
}