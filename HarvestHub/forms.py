from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class FarmerRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter User Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Confirm Password'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(format='%Y/%m/%d', attrs={'class': 'form-control', 'placeholder': 'YYYY/MM/DD'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}))

    class Meta:
        model = Farmer
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'city', 'Image', 'phone_number']
        
        
class FarmerRegistrationTestForm(UserCreationForm):
    username = username = forms.CharField(
       # label='UserName',
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'id': 'username'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control border-primary', 'id': 'email'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control border-primary', 'id': 'password1'})
    )
    password2 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control border-primary', 'id': 'password2'})
    )
    
    city = forms.CharField(
        label='City',
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'id': 'city'})
    )
    
    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={'class': 'form-control border-primary', 'id': 'phone'}),
        max_length=14,
        help_text='Enter your phone number in the format +94-XXXXXXXXX'
    )
    Image = forms.ImageField(
        label='File',
        widget=forms.ClearableFileInput(attrs={'class': 'border-primary', 'id': 'file'})
    )
    
    gender = forms.ChoiceField(choices=[('', 'Select The Gender'),
                                      ('Male', 'Male'),
                                      ('Female', 'Female'),
                                      ('Other', 'Other')],
                             widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Farmer
        fields = ['username', 'email', 'password1', 'password2', 'city', 'phone_number', 'Image', 'gender']