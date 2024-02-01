from django.urls import path
from . import views

urlpatterns = [
    path('landowners/', views.landowner_list, name='landowner_list'),
    path('landowners/<int:landowner_id>/', views.property_list, name='property_list'),

]
