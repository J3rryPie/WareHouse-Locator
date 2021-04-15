from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import City
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True
        self.fields['email'].required = True
        self.fields['password1'].required = True
        self.fields['password2'].required = True
    class Meta:
        model=User
        fields=['username','email','password1','password2']
# class City_Choice_Form(forms.ModelForm):
#     class Meta:
#         model = City
#         fields = [‘__all__’]

class City_Choice_Form(forms.Form):

    OPTIONS = [
        ('1','Mumbai'),
        ('2','Pune'),
        ('3','Nashik'),
        ('4','Nagpur'),
        ('5','Thane'),
        ('6','Alibaug'),
        ('7','Kolhapur'),
        ('8','Solapur'),
        ('9','Latur'),
        ('10','Nanded'),
        ('11','Lucknow'),
        ('12','Chennai'),
        ('13','Kolkata'),
        ('14','Banglore'),
        ('15','Delhi'),
        ]

    citi = forms.MultipleChoiceField(
            choices=OPTIONS,
            initial='0',
            # widget=forms.SelectMultiple(),
            widget=forms.CheckboxSelectMultiple,
            required=True,
            label='City Choices',
        )
    k = forms.IntegerField(initial=1)