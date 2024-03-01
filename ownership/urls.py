from django.urls import path
from .views import LandListView
from . import views

urlpatterns = [
    path('', LandListView.as_view(), name='ownership-home'),
    path('about/', views.about, name='ownership-about'),
]