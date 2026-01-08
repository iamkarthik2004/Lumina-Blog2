from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_post_view, name='create_post'),
    path('edit/<int:pk>/', views.edit_post_view, name='edit_post'),
    path('delete/<int:pk>/', views.delete_post_view, name='delete_post'),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/<int:pk>/dislike/', views.dislike_post, name='dislike_post'),
]
