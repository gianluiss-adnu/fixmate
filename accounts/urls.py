from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),

    #dashboards
    path("customer/dashboard/", views.customer_dashboard),
    path("provider/dashboard/", views.provider_dashboard),
]