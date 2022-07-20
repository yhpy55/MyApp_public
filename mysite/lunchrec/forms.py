from django import forms
from .models import LunchrecList


class LunchrecListForm(forms.ModelForm):
    class Meta:
        model = LunchrecList
        fields = ['date', 'shop_name', 'menu_name', 'price', 'remarks']
