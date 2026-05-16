from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),

    #dashboards
    path("customer/dashboard/", views.customer_dashboard, name="customer_dashboard"),
    path("provider/dashboard/", views.provider_dashboard, name="provider_dashboard"),
    path("logout/", views.logout_view, name="logout"),
]