from django import forms
from .models import Gourmet


class FindForm(forms.Form):
    find = forms.CharField(label='検索条件(店舗名 or 駅名 or ジャンル or 定休日 or 禁煙)', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
