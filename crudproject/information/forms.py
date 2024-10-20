from django import forms
from . models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile_number', 'date_of_birth', 'photo', 'password']

