from django.shortcuts import render
from .models import Profile
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def _redirect_back(request):
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    else:
        return redirect('home')

@login_required
def profile_view(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    posts = Post.objects.filter(author=profile.user)
    return render(request, 'pages/profile.html', {'profile': profile, 'posts': posts})

@login_required
def profile_search_results_view(request, query):
    profiles = Profile.objects.filter(display_name__icontains=query)
    return render(request, 'pages/profile_list.html', {'profiles': profiles})

@login_required
def follow(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    profile.followers.add(request.user.profile)
    return redirect('profile_view', username=username)