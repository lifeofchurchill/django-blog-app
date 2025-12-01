from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        #special django form based on post model
        #fields included are what we want to see for the form
        model = Post
        fields = ['title', 'slug', 'content', 'excerpt', 'featured_image', 'category', 'tags', 'status']
