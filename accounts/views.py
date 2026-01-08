from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from blog.models import Post

def login_view(request):
    # Determine the template path based on file location
    # Since we configured DIRS to include BASE_DIR/templates, we can just use 'login.html'
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def home_view(request):
    posts = Post.objects.all()
    
    # Get all unique categories from existing posts
    # We use a set comprehension to get unique values, then sort them
    categories = sorted(list(set(post.category for post in posts if post.category)))
    
    # Filter by category if requested
    selected_category = request.GET.get('category')
    if selected_category:
        posts = posts.filter(category=selected_category)
        
    return render(request, 'index.html', {
        'posts': posts, 
        'categories': categories,
        'selected_category': selected_category
    })
