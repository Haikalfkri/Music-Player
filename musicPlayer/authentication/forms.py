from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'username',
                'id': 'username',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'first_name',
                'id': 'first_name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'name': 'last_name',
                'id': 'last_name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'name': 'email',
                'id': 'email',
            }),
        }