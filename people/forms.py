from django import forms
from .models import Person

# this is how I connect my models to be edited from the front end. really nice because i dont have to go back through url /admin

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person 
        fields = (
            'profile_picture',
            'first',
            'middle',
            'last', 
            'header', 
            'birthday', 
            'phone', 
            'phone2', 
            'insta',
            'address',
            'notes',
            'prayers',
            )

        widgets = {
            'first': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Something catchy!'}),
            'middle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Something catchy!'}),
            'last': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Something catchy!'}),
            'header': forms.TextInput(attrs={'class': 'form-control',}),
            'phone': forms.TextInput(attrs={'class': 'form-control',}),
            'phone2': forms.TextInput(attrs={'class': 'form-control',}),
            'insta': forms.TextInput(attrs={'class': 'form-control',}),
            'email': forms.EmailInput(attrs={'class': 'form-control',}),
            'addess': forms.TextInput(attrs={'class': 'form-control',}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
            'prayers': forms.Textarea(attrs={'class': 'form-control'}),
        }



