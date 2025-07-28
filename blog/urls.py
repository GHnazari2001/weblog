from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('post/new',views.PostNewView.as_view(), name='new_post'),
    path('author/<str:username>/', views.AuthorPostListView.as_view(), name='posts_by_author'),
    path('post/<int:pk>',views.PostDetailView.as_view(), name='post_detail'),
    path('post/update/<int:pk>',views.UpdatePostView.as_view(), name='update_post'),
    path('post/delete/<int:pk>',views.DeletePostView.as_view(), name='delete_post'),
    path('post/<int:pk>/like/',views.LikePostView.as_view(), name='post_like'),
    path('search/', views.SearchView.as_view(), name='search_results'),
    path('category/<str:category_slug>/', views.CategoryPostListView.as_view(), name='posts_by_category'),
    path('tag/<str:tag_slug>/', views.TaggedPostListView.as_view(), name='posts_by_tag'),
]
