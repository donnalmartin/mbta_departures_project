from django import forms
from .models import StationModel

class BoardViewForm(forms.ModelForm):
    class Meta:
        model = StationModel
        fields = ['name']