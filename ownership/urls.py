from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ownership-home'),
    path('about/', views.about, name='ownership-about'),
    path('landowner_form/', views.Landowner_Form, name='landowner-form'),
    path('landproperty_form/', views.Landproperty_Form, name='landproperty-form'),
    path('landowners/', views.landowner_list, name='landowner-list'),
    path('landowners/<int:landowner_id>/', views.property_list, name='property-list'),

]
