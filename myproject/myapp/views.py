from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreateUserForm

from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = CreateUserForm()
    return render(request, 'register_page.html', {'form': form})
def index(request):
    return render(request,"home.html")


def Profile(request):
    return render(request, "profile.html")



def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'Welcome back, {username}! You are now logged in.')
            return redirect('home')  # Adjust the URL name to your home page
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')

    return render(request, 'login_page.html')







def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')