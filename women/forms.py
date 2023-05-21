
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class AddPostForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label="Категория не выбрана"
    class Meta:
        model=Women
        fields= ['title','slug','content','photo','is_published','cat']
        
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':100, 'rows':20}),
        }

  
class RegisterUserForm(UserCreationForm):
    username= forms.CharField(label="Login", widget=forms.TextInput(attrs ={'class':'form-input'}))
    email=forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label="Parol", widget=forms.PasswordInput(attrs ={'class':'form-input'}))
    password2= forms.CharField(label="Parol again", widget=forms.PasswordInput(attrs ={'class':'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class':'form-input'}))
    password =forms.CharField(label ='Parol', widget=forms.PasswordInput(attrs={'class':'form-input'}))
       