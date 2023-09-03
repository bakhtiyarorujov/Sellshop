from typing import Any, Dict
from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=50, widget = forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))
    full_name = forms.CharField(max_length=150, widget=forms.TextInput({
        'placeholder': 'Fullname here'
    }))

    class Meta:
        model = User
        fields = {
            'email',
            'phone',
            'password',
            'newsletter',
            'first_name',
            'last_name'
        }

        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email address'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone number'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password'
            })
        }

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords does not match!')
        return super().clean()
    
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput({
        'placeholder': 'Email address'
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput({
        'placeholder': 'Password'
    }))