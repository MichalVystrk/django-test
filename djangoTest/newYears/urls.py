from django.urls import path
from . import views

urlpatterns = [
    path('', views.isIt, name='isIt'),
]