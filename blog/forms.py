from django import forms
from .models import Post, Comment,Category


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        label="برچسب‌ها", 
        required=False, 
        help_text='تگ‌های مورد نظر را با یک کاما (,) از هم جدا کنید.'
    )
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'body','category', 'photo','tags']
      
      
    def __init__(self, *args, **kwargs):
     
        user = kwargs.pop('user', None) 
        super().__init__(*args, **kwargs)
        
       
   
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
