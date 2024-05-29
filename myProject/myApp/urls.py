from . import views
from django.urls import path

urlpatterns = [
    path('insert-sensor/', views.insert_sensor, name='insert_sensor'),
    path('insert-user/', views.insert_user, name='insert_user'),
    path('', views.home_view, name='home'),
]