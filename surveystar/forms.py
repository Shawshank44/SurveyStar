from django import forms
from django.db.models import fields
from django.forms import widgets
# from django.forms.models import labels
from .models import Customer
from datetime import datetime

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]
STYLE_CHOICES=[
    ('Veg','Veg'),
    ('Non-Veg','Non-Veg')
]

class Customer_form(forms.ModelForm):
     gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect,)
     foodstyle = forms.ChoiceField(choices=STYLE_CHOICES,widget=forms.RadioSelect)
     class Meta :
         model = Customer
         fields = ['name','gender','Mobilenumber','email','foodstyle','preference','opinion']
         labels = {'name':'Name','gender':'Gender','Mobilenumber':'Phone number','email':'E-mail','foodstyle':'What do you prefer','preference':'Favourite style','opinion':'Message'}
         widgets = {
             'name' : forms.TextInput(attrs={'class':'form-control'}),
             'Mobilenumber' : forms.TextInput(attrs={'class':'form-control'}),
             'email' : forms.TextInput(attrs={'class':'form-control'}),
             'preference' : forms.Select(attrs={'class':'form-select'}),
             'opinion' : forms.Textarea(attrs={'class':'form-control'}),
        }