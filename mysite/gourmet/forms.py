from django import forms
from .models import Gourmet


class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
