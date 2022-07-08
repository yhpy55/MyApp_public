from django import forms
from .models import Gourmet


class FindForm(forms.Form):
    find = forms.CharField(label='検索条件を指定してください。（店舗名、駅名、ジャンル、定休日、禁煙）', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
