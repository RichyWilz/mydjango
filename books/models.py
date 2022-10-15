
from django.db import models
from datetime import date, timedelta
from django.contrib.auth.models import User

# Create your models here.

# This is the book model, which refers to an actual book in the library. 
# has a title,publication_date,subject,author,description,cover-photo and its status(whether its available or not)
class Book(models.Model):
    STATUS = (
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    )
    title            = models.CharField(max_length=40)
    publication_date = models.DateField(auto_now=True)
    subject_area     = models.CharField(max_length=15)
    author           = models.CharField(max_length=40)
    description      = models.TextField()
    cover_photo      = models.ImageField(null=True, blank=True, upload_to='static/images/')
    status           = models.CharField(max_length=15, choices=STATUS, default='Available')

    def __str__(self) :
        return self.title


# This is the borrowed book model, which refers to a book that is borrowed from the library.contains a booktitle,borrowdate
# emailaddress and featured properties that enable a student to know the days remaining,return date and fine as 
# time progresses. It has a one to many relationship with the book model as expressed in the "book_title" field 
class Borrow(models.Model): 
    book_title    = models.ForeignKey('Book', on_delete=models.CASCADE)
    borrow_date   = models.DateField(auto_now=True)
    email_address = models.EmailField('Email Field')

    def __str__(self):
        return self.book_title.title
    # use this in table that will keep track of days
    @property
    def days_remaining(self):
        today = date.today()
        days_remaining= self.return_date - today
        return days_remaining.days

    @property
    def return_date(self):
        that_date = self.borrow_date + timedelta(days=3)
        return that_date

    @property
    def Fine(self):
        dafine = 0
        if self.days_remaining < -3:
            dafine = "5000"

        elif self.days_remaining <= -15:
            dafine = "15000"

        else:
            dafine = "None"

        return dafine

   

    
    



    
        

