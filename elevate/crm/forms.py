
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from .models import CustomUser
from django.forms.widgets import PasswordInput,TextInput


# Create a user/register

class CreateUserForm(UserCreationForm):

    birthday = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False, help_text='Format: YYYY-MM-DD')
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False, help_text='Enter your address here.')

    class Meta:

        model = CustomUser
        fields = ['first_name','last_name','username', 'email','password1','password2','birthday','address']
    
# Authenticate the user
        
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    















