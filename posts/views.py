from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Post, Like

def redirect_back(request):
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    else:
        return redirect('home')

def posts(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        post = Post.objects.create(author=request.user, content=content)
        return redirect_back(request)

    return JsonResponse({'error': f'Invalid request method {request.method}'})

def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect_back(request)