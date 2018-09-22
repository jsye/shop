"""
this is user App model forms
                            --by zero
"""
from django import forms

from user.models import Usermodel


class Userform(forms.ModelForm):
    class Meta:
        model = Usermodel
        fields = ['mobile', 'password']
