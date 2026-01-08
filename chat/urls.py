from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_users, name='search_users'),
    path('u/<str:username>/', views.profile_view, name='profile_view'),
    path('chat/<str:username>/', views.chat_view, name='chat_view'),
    
    # APIs
    path('api/send/', views.send_message_api, name='send_message_api'),
    path('api/messages/<str:username>/', views.get_messages_api, name='get_messages_api'),
]
