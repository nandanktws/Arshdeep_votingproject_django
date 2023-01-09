from django import forms

class Voterage(forms.Form):
    age = forms.CharField(label='age', max_length=200)