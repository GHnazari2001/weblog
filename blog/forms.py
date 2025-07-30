from django import forms
from .models import Post, Comment,Category


class PostForm(forms.ModelForm):
  
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'body', 'category', 'photo', 'tags']
        help_texts = {
            'tags': 'تگ‌های مورد نظر را با یک کاما (,) از هم جدا کنید.',
        }
      
    def __init__(self, *args, **kwargs):
     
        user = kwargs.pop('user', None) 
        super().__init__(*args, **kwargs)
        
       
   
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
