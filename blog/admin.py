from django.contrib import admin
from .models import Post,Comment ,Category
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug') # فیلدهایی که در لیست دسته‌بندی‌ها نمایش داده می‌شوند
    prepopulated_fields = {'slug': ('name',)} # اسلاگ به طور خودکار بر اساس نام ساخته می‌شود
    search_fields = ('name',) # امکان جستجو بر اساس نام دسته‌بندی

