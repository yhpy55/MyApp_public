from django import forms
from .models import Sauna


class SaunaForm(forms.ModelForm):
    class Meta:
        model = Sauna
        fields = ['name', 'address', 'fee', 'holiday']
