from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

from . models import Role 


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.ModelChoiceField(queryset=Role.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'role']