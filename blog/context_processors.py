from .models import Post,Category
from django.db.models import Count
from taggit.models import Tag

def recent_posts(request):
    recent_posts=Post.objects.order_by('-date')[:5]
    return {'recent_posts':recent_posts}



def common_sidebar_data(request):
    all_tags = Tag.objects.all()
    categories_with_posts = Category.objects.annotate(
        num_posts=Count('posts')
    ).filter(num_posts__gt=0).order_by('name')

    context = {
        'all_categories_sidebar': categories_with_posts,
        'all_tags_sidebar': all_tags, 
    }
    return context