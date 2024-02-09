from django import forms
from .models import Landowner, LandProperty

class LandownerForm(forms.ModelForm):
    class Meta:
        model = Landowner
        fields = ['name', 'address', 'phone_number', 'email', 'inputter']

class LandPropertyForm(forms.ModelForm):
    class Meta:
        model = LandProperty
        fields = ['landowner', 'address', 'phone_number', 'email', 'land_type', 'other_details']
