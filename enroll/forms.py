from dataclasses import field, fields
from django.core import validators 
from django import forms
from .models import user1,addtech,addgit

class Register(forms.ModelForm):
    class Meta:
        model=user1
        fields=['name','email','password']
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email' :forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            
        }
    
