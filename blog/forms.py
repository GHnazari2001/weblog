from django import forms
from .models import Post, Comment,Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'body','category', 'date', 'photo']
        # widgets = {
           
        #     'tags': forms.CheckboxSelectMultiple,         # نمایش تگ‌ها به صورت چک‌باکس
        #     'category': forms.Select(), # این ویجت پیش‌فرض برای ForeignKey است (دراپ‌دان)
        # }
    def __init__(self, *args, **kwargs):
     
        user = kwargs.pop('user', None) 
        super().__init__(*args, **kwargs)
        
       
   
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
