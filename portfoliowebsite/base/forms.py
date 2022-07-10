from django import forms

class Refresh(forms.Form):
    name = forms.CharField(label="Nickname", max_length=200)