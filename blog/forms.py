from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'image', 'category', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-[#1a2232] border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'Enter Title'}),
            'subtitle': forms.TextInput(attrs={'class': 'w-full bg-[#1a2232] border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'Enter Subtitle'}),
            'image': forms.FileInput(attrs={'class': 'w-full text-sm text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-primary file:text-white hover:file:bg-blue-600 cursor-pointer'}),
            'category': forms.TextInput(attrs={'class': 'w-full bg-[#1a2232] border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-primary', 'placeholder': 'e.g. Tech, Art'}),
            'content': forms.Textarea(attrs={'class': 'w-full bg-[#1a2232] border border-white/10 rounded-xl px-4 py-3 text-white focus:outline-none focus:ring-2 focus:ring-primary h-40', 'placeholder': 'Write your story...'}),
        }
