import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lumina_core.settings')
django.setup()

from blog.models import Post

# Clear all posts
count = Post.objects.count()
Post.objects.all().delete()

print(f"Deleted {count} posts.")
