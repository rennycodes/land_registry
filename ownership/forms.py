from django import forms
from .models import Landowner, Property

class LandownerForm(forms.ModelForm):
    class Meta:
        model = (Landowner, Property)
        fields = ['name', 'contact_number', 'landowner', 'address']
