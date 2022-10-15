
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length= 15, help_text= '*' )
    first_name = forms.CharField(max_length = 30, help_text= '*')
    last_name = forms.CharField(max_length = 30, required=False) #help_text= 'Optional')
    email = forms.EmailField(max_length=200) #help_text = 'Enter valid e-mail address')
    course = forms.CharField(max_length= 35, required= True , help_text='*')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'course',
        ]

        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control","placeholder":"Enter your username"}),
             'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your first name'}),
             'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your last name'}),
             'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email address'}),
             'course': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your course'}),
            'password': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your password'}),
             'password1': forms.TextInput(attrs={'class': 'form-control','placeholder':'Confirm your password'}),
         }
         
