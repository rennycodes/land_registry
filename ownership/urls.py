from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ownership-home'),
    path('landowners/', views.landowner_list, name='landowner_list'),
    path('landowners/<int:landowner_id>/', views.property_list, name='property_list'),

]
