from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Message

@login_required
def search_users(request):
    query = request.GET.get('q', '')
    users = []
    if query:
        users = User.objects.filter(
            Q(username__icontains=query) | 
            Q(email__icontains=query)
        ).exclude(id=request.user.id)
    else:
        # Show some random users or recent users if no query
        users = User.objects.exclude(id=request.user.id)[:10]
        
    return render(request, 'search.html', {'users': users, 'query': query})

from blog.models import Post

@login_required
def profile_view(request, username):
    user_profile = get_object_or_404(User, username=username)
    user_posts = Post.objects.filter(author=user_profile).order_by('-created_at')
    return render(request, 'profile.html', {'profile_user': user_profile, 'user_posts': user_posts})

@login_required
def chat_view(request, username):
    other_user = get_object_or_404(User, username=username)
    # Filter messages between the two users
    messages = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) |
        Q(sender=other_user, receiver=request.user)
    ).order_by('timestamp')
    
    last_id = messages.last().id if messages else 0
    
    return render(request, 'chat.html', {
        'other_user': other_user,
        'messages': messages,
        'last_id': last_id
    })

# API Endpoints for AJAX
@csrf_exempt
@login_required
def send_message_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        receiver_username = data.get('receiver')
        content = data.get('content')
        
        try:
            receiver = User.objects.get(username=receiver_username)
            message = Message.objects.create(
                sender=request.user,
                receiver=receiver,
                content=content
            )
            
            return JsonResponse({
                'status': 'success', 
                'id': message.id,
                'message': content, 
                'timestamp': message.timestamp.strftime("%b %d, %H:%M")
            })
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
            
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def get_messages_api(request, username):
    other_user = get_object_or_404(User, username=username)
    last_id = request.GET.get('last_id', 0)
    
    # Get new messages from the other user
    messages = Message.objects.filter(
        sender=other_user, 
        receiver=request.user,
        id__gt=last_id
    ).order_by('timestamp')
    
    data = []
    for msg in messages:
        data.append({
            'id': msg.id,
            'sender': msg.sender.username,
            'content': msg.content,
            'timestamp': msg.timestamp.strftime("%b %d, %H:%M"),
            'is_me': False
        })
        
    return JsonResponse({'messages': data})
