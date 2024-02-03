from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ownership-home'),
    path('ownership_form/', views.Landowner_Form, name='ownership-form'),
    path('landowners/', views.landowner_list, name='landowner-list'),
    path('landowners/<int:landowner_id>/', views.property_list, name='property_list'),

]
