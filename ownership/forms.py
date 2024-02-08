from django import forms
from .models import Landowner, LandProperty

class LandownerForm(forms.ModelForm):
    class Meta:
        model = Landowner
        fields = ['name', 'address', 'phone_number', 'email', 'inputter_name']

class LandPropertyForm(forms.ModelForm):
    class Meta:
        model = LandProperty
        fields = ['landowner', 'coordinates', 'land_type', 'other_details', 'inputter_name']
