from django.urls import path
from . import views

urlpatterns = [
    path('<int:value>/', views.narsha_single_pages),
    path('', views.index),
]
