from django.urls import path
from . import views

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('<int:id>/', views.service_detail, name='service_detail'), # '<int:id>/' determines which service to show
    path('detail/', views.service_detail_test, name='service_detail_test')
]