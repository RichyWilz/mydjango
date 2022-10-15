
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html', {})

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('accounts:login')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('books:book_overview')
        else:
            messages.success(request, ("There was an error logging in, please try again...."))
            return redirect('accounts:login')
    else:
        return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ("you logged out"))
    return redirect("accounts:login")   
  



