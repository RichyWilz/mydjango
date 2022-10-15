from django.shortcuts import render, redirect
from .models import Book, Borrow
from .forms import BorrowForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.db.models import Q



# Create your views here.

# This view function on request will take in the dictionary which contains the different created books' models
# and their keys and when called, will need the user template to use the keys (which are generally "books")
# to access the actual book data in the database.However this needs the user to be logged in.

@login_required(login_url='/login/')
def book_overview(request):
    books = Book.objects.all().order_by('title')
    context = {
        'books': books
    }
    return render(request, 'book_overview.html', context)

# This view function on request will take the primary key of a specified book and connect it to the book detail from the database
# to the template. it contains a dictionary that takes a key(detail) and maps it to an actual book data stored in database.
# it also needs one to be logged in

@login_required(login_url='/login/')
def book_detail(request, pk):
    detail = Book.objects.get(pk= pk)
    context = {
        'detail': detail
    }
    return render(request,'book_detail.html', context)

# This view function on request will make user(student) able to fill in a form for a specific book through primary key(pk)
#  borrowing a book where it'll first check
# whether the user is trying to take an already unavailable book and if so will redirect them to a page with an error 
# message or else will take their details in the form and make the book they are reserving unavailable.if the student has
# successfully reserved/borrowed the book, it'll redirect them to a page which will show the book taken and success message
# Needs one to be logged in to use it.

@login_required(login_url='/login/')
def borrow(request, pk):
    borrowbook = Book.objects.get(pk= pk)
    form = BorrowForm(request.POST or None)
    if request.method == "POST":
        if borrowbook.status == "Unavailable":
            messages.success(request, ("Oops....book is unavailable, please try again someother time"))
            return  redirect('books:message')
        if form.is_valid():
            form.save()
            messages.success(request, ("You've successfully reserved a book,you are required to get it in the next 24 hours from the library with your School ID.Check activity"))
            borrowbook.status = "Unavailable"
            borrowbook.save() 
            return redirect ('books:activity') 
    context = {
        'form': form
    }
    return render(request, 'borrow.html',context)

# This view function on request will show an html template which will house an error message.
#  this needs the user to be logged in too.

@login_required(login_url='/login/')
def urlmessage(request):
    return render(request, 'urlmessage.html',{})

# This view function on request contains dictionary which takes in a key (laforms) and links it to an actual
# borrow model in the html template called activity
    
@login_required(login_url='/login/')
def activity(request):
    laforms = Borrow.objects.all
    context ={
        'laforms' : laforms
    }
    return render(request, 'activity.html',context)

# Implementing the search function using a class that uses different fields.
class BookSearchView(generic.ListView):

    model = Book
    template_name = 'search_book.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Book.objects.filter(
            Q(title__icontains = query) | Q(subject_area__icontains = query) | 
            Q(author__icontains = query)
            )
