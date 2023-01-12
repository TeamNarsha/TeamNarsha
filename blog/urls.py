from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('<int:value>/', views.narsha_single_pages),
    path('', views.index),
]
