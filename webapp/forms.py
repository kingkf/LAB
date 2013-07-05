from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='username', max_length=30)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password',widget=forms.PasswordInput())
    password2 = forms.CharField(label='retype',widget=forms.PasswordInput())

    def clean_username(self):
        username = self.clean_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError ('name error')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
            raise forms.ValidationError('name exsit')
    
    def clean_email(self):
        email = self.clean_data['email']
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
            raise forms.ValidationError ('email exsit')
    
    def clean_password2(self):
        if 'password1' in self.clean_data:
            password1 = self.clean_data['password1']
            password2 = self.clean_data['password2']
        if password1 == password2:
            return password2
            raise forms.ValidationError('password not fit')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
