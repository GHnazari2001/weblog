from django.db import models
from datetime import date
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager
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
    title = models.CharField(max_length=255 , verbose_name="عنوان")
    excerpt = models.TextField(verbose_name="خلاصه")
    body = models.TextField(verbose_name="متن کامل")
    author = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE , verbose_name="نویسنده")
    date =date = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ انتشار")
    photo = models.ImageField(upload_to='photo/%Y/%m/%d' ,  verbose_name="تصویر ")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True,blank=True,             
        related_name='posts',     
        verbose_name="دسته‌بندی"
    )
    likes= models.ManyToManyField(settings.AUTH_USER_MODEL ,
        related_name= "blog_posts_liked",
        blank=True ,
        verbose_name='پسندیدن'
    )
    tags = TaggableManager(verbose_name="برچسب‌ها", blank=True)
    class Meta:
        ordering = ['-date']
        
    def number_of_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
    
    

class Comment(models.Model):
    author = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE ,verbose_name="نویسنده")
    post = models.ForeignKey(Post, on_delete=models.CASCADE , verbose_name=" پست")
    body = models.TextField(null=False, blank=False ,verbose_name="متن دیدگاه")
    date = models.DateTimeField(default=timezone.now , verbose_name="تاریخ انتشار")

    def __str__(self):
        return self.body
    
