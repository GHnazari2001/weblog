from django.urls import path
from .views import HomeView, PostNewView,PostDetailView,UpdatePostView, DeletePostView,SearchView,CategoryPostListView


urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('post/new',PostNewView.as_view(), name='new_post'),
    path('post/<int:pk>',PostDetailView.as_view(), name='post_detail'),
    path('post/update/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('post/delete/<int:pk>',DeletePostView.as_view(), name='delete_post'),
    path('search/', SearchView.as_view(), name='search_results'),
      path('category/<slug:category_slug>/', CategoryPostListView.as_view(), name='posts_by_category'),
 
]
