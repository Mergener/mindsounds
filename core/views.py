from django.shortcuts import render
from django.contrib.auth import login

def base_view(request):
    # Check if the user is logged in.
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return unlogged_home(request)

def unlogged_home(request):
    return render(request, 'unlogged_home.html')

def feed_view(request):
    pass

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    return render(request, 'core/login.html')
