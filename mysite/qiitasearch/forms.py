from django import forms
from .models import QiitaSearch


class FindForm(forms.Form):
    find = forms.CharField(label='検索条件(記事タイトル、タグ)', required=False,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
