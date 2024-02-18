from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ownership-home'),
    path('about/', views.about, name='ownership-about'),
]