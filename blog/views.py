from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
import random

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.color = random.choice(['primary', 'green-400', 'purple-400', 'pink-400']) # Random color for diversity
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form, 'title': 'Create Post'})

from django.shortcuts import get_object_or_404
from .models import Post

@login_required
def edit_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'create_post.html', {'form': form, 'title': 'Edit Post', 'post': post})

@login_required
def delete_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.author:
        post.delete()
    return redirect('home')

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return redirect('post_detail', pk=pk)

@login_required
def dislike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
        
    return redirect('post_detail', pk=pk)
