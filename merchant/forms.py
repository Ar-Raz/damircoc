from django import forms
from django.conf import settings

ACCOUNT_CHOICES = (
    ("A","تامین کننده"  ),
    ("B", "مشتری ")
)

class RegisterationForm(forms.Form):
    account_type = forms.ChoiceField(widget=forms.RadioSelect(),choices=ACCOUNT_CHOICES)
