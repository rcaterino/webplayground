from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Campo obligatorio, con máximo 254 caracteres y debe sere válido ')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Ya este email está registrado en nuestro sistema, inténtelo nuevamente con otro email')
        return email