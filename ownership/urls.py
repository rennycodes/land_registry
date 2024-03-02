from django.urls import path
from .views import (LandListView,
                    LandDetailView,
                    LandCreateView,
                    LandUpdateView)
from . import views

urlpatterns = [
    path('', LandListView.as_view(), name='ownership-home'),
    path('land/<int:pk>/', LandDetailView.as_view(), name='land-detail'),
    path('land/new', LandCreateView.as_view(), name='land-create'),
    path('land/<int:pk>/update', LandUpdateView.as_view(), name='land-update'),
    path('about/', views.about, name='ownership-about'),
]
