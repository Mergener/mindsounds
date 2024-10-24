from django.shortcuts import render, redirect
from .models import Profile, Follower
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

    posts = list(Post.objects.filter(author=profile.user))
    posts.sort(key=lambda x: x.created_at, reverse=True)

    if user.username != request.user.username:
        is_following = Follower.objects.filter(user=profile.user, follower=request.user).exists()
    else:
        is_following = False

    return render(request, 'pages/profile.html', {'profile': profile, 'posts': posts, 'is_following': is_following})

@login_required
def profile_search_results_view(request):
    name_like = request.GET.get('name_like')
    profiles = Profile.objects.filter(user__username__icontains=name_like)
    return render(request, 'pages/profile_list.html', {'profiles': profiles})

@login_required
def follow(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    Follower.objects.create(user=profile.user, follower=request.user)
    return _redirect_back(request)

@login_required
def unfollow(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    Follower.objects.filter(user=profile.user, follower=request.user).delete()
    return _redirect_back(request)

@login_required
def followers_view(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    followers = Follower.objects.filter(user=profile.user)
    profiles = [follower.follower.profile for follower in followers]
    return render(request, 'pages/profile_list.html', {'profiles': profiles})

@login_required
def following_view(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    following = Follower.objects.filter(follower=profile.user)
    profiles = [follow.user.profile for follow in following]
    return render(request, 'pages/profile_list.html', {'profiles': profiles})