from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm

def base_view(request):
    # Check if the user is logged in.
    if request.user.is_authenticated:
        print("authenticated!")
        return render(request, 'pages/feed.html')
    else:
        print("not authenticated!")
        return unsigned_home(request)

def unsigned_home(request):
    return render(request, 'pages/unsigned_home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('base_view')
    else:
        form = SignupForm()

    return render(request, 'pages/signup.html', {'form': form})

def login_view(request):
    wrongCredentials = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('base_view')
            else:   
                wrongCredentials = True
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'wrongCredentials': wrongCredentials, 'form': form})

def logout_view(request):
    logout(request)
    return redirect('base_view', permanent=True)
