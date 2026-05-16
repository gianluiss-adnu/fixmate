
from django.urls import path
from . import views

urlpatterns = [
    path('booking/<int:booking_id>/accept/', views.accept_booking, name='accept_booking'),
    path('booking/<int:booking_id>/reject/', views.reject_booking, name='reject_booking'),
    path("book/<int:service_id>/", views.create_booking, name="create_booking"),
]