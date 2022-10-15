from django import forms
from django.forms import ModelForm
from .models import Borrow

# This is a model form which enables a student to be able to create a "borrow" book which essentially means 
# the student will be borrowing a book. The form will only need the student to fill in their email and book id.which 
# is the primary key
class BorrowForm(ModelForm):
    class Meta:
        model = Borrow
        fields = ['book_title',
            'email_address',
            ]
        widgets = {
            'book_title': forms.TextInput(attrs={"class": "form-input","placeholder":"Enter book ID"}),
             'email_address': forms.EmailInput(attrs={'class': 'form-input','placeholder':'Enter your email address eg someone@gmail.com'}),
         }
        labels = {
            'book_title':'Book ID',
            'email_address':'Email',
        }
