from django import forms
from django.forms import TextInput
from django.contrib.auth.models import User


usernameInputWidgets = {
    'placeholder': 'Логін', 
    'aria-label': 'Username', 
    'aria-describedby': 'basic-addon1', 
    'class': 'form-control', 
    'type':'text'
}

passwordInputWidgets = {
    'placeholder': 'Пароль', 
    'aria-label': 'Password', 
    'aria-describedby': 'basic-addon1', 
    'class': 'form-control', 
    'type':'password'
}


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')
    email = forms.EmailField(label='Почта')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=TextInput(attrs=usernameInputWidgets))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs=passwordInputWidgets))


class ReturnTicketForm(forms.Form):
    number = forms.CharField(label='Номер билета:')


class BuyingTicketForm(forms.Form):
    sector = forms.CharField(label='Номер сектора')
    place = forms.CharField(label='Место')


