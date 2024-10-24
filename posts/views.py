from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Post, Like
from django.contrib.auth.decorators import login_required

def _redirect_back(request):
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    else:
        return redirect('home')

@login_required
def posts(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        post = Post.objects.create(author=request.user, content=content)
        return _redirect_back(request)

    return JsonResponse({'error': f'Invalid request method {request.method}'})
    
@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return _redirect_back(request)