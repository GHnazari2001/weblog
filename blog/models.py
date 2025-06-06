from django.db import models
from datetime import date
from django.utils import timezone
from django.urls import reverse
# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category Name")
    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True, verbose_name="Slug")
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('posts_by_category', kwargs={'category_slug': self.slug})




class Post(models.Model):
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True,             
        related_name='posts',     
        verbose_name="Category"
    )

    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
    

class Comment(models.Model):
    author = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body
    
