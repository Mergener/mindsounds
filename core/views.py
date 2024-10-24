from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm
from profiles.models import Profile, Follower
from posts.models import Post

def _get_posts_from_following(user):
    following = Follower.objects.filter(follower=user)

    # Add the user themselves to the list of users to get posts from
    following = list(following)
    following.append(Profile.objects.get(user=user))

    all_posts = []
    for follow in following:
        all_posts += Post.objects.filter(author=follow.user)

    all_posts.sort(key=lambda x: x.created_at, reverse=True)
    return all_posts

def home(request):
    if request.user.is_authenticated:
        return render(request, 'pages/signed_home.html', {'posts':_get_posts_from_following(request.user)})
    else:
        return render(request, 'pages/unsigned_home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')
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
                return redirect('home')
            else:   
                wrongCredentials = True
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'wrongCredentials': wrongCredentials, 'form': form})

def logout_view(request):
    logout(request)
    return redirect('home', permanent=True)
