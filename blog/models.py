from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    category = models.CharField(max_length=50) # e.g. Tech, Art, Lifestyle
    color = models.CharField(max_length=50, default="primary") # e.g. primary, purple-400
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    read_time = models.IntegerField(default=5)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
