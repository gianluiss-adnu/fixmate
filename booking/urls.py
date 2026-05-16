
from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_page, name='booking_page'),
    path('booking/<int:booking_id>/accept/', views.accept_booking, name='accept_booking'),
    path('booking/<int:booking_id>/reject/', views.reject_booking, name='reject_booking'),
]