from django.shortcuts import render,get_object_or_404
from django.views.generic import View ,CreateView,DetailView,FormView,ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post,Category,Comment
from .forms import PostForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.core.paginator import Paginator
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.http import JsonResponse
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

# class HomeView(View):
#     #model = Post
#     template_name = 'home.html'
#     paginate_by = 2
    
#     def get(self ,request):
#         posts = Post.objects.all()
#         paginator = Paginator(posts ,self.paginate_by)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
       
#         return render(request ,self.template_name , {'post_list': page_obj})
# A cleaner HomeView using ListView
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'
    paginate_by = 2

    
class CommentGet(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

class PostDetailView(View):

    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
    

class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "post_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("post_detail", kwargs={'pk': post.pk})

    
    

# class PostNewView(CreateView):
#     model = Post
#     template_name = 'new_post.html'
#     form_class = PostForm
#     success_url =reverse_lazy('home')
    
class PostNewView(LoginRequiredMixin, CreateView): 
    model = Post
    template_name = 'new_post.html'
    form_class = PostForm
    success_url = reverse_lazy('home')
   

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Add this import at the top
from django.contrib.auth.mixins import UserPassesTestMixin

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm

    def test_func(self):

        post = self.get_object()
        return self.request.user == post.author

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def test_func(self):
    
        post = self.get_object()
        return self.request.user == post.author    
    
    
    
    
# class UpdatePostView(UpdateView):
#     model = Post
#     template_name = 'update_post.html'
#     fields = ['title', 'excerpt', 'body','photo']
    


# class DeletePostView(DeleteView):
#     model = Post
#     template_name = 'delete_post.html'
#     success_url = reverse_lazy('home')

class SearchView(ListView):
    model = Post
    template_name = 'search_result.html'
    context_object_name = 'post_list'
    paginate_by = 2 # یا هر تعداد که برای صفحه‌بندی در نظر دارید

    def get_queryset(self):
        query = self.request.GET.get('q') # دریافت عبارت جستجو
        
        if query: 
            queryset = Post.objects.filter(
                Q(title__icontains=query) | 
                Q(body__icontains=query) | 
                Q(excerpt__icontains=query)
            ).order_by('-date').distinct() 
        else:
            
            queryset = Post.objects.none()
            
        return queryset 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
    
class CategoryPostListView(ListView):
    model = Post
    template_name = 'category_posts.html'
    context_object_name = 'post_list'
    paginate_by = 2 

    def get_queryset(self):

        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        queryset = Post.objects.filter(category=self.category).order_by('-date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      
        context['category'] = self.category
        return context
    
    
class LikePostView(LoginRequiredMixin , View):
    def post(self,request ,pk,*args, **kwargs):
        post = get_object_or_404(Post , pk = pk)
        user = self.request.user
        
        is_liked = False
        if user in post.likes.all():
            post.likes.remove(user)
            is_liked = False
        else :
            post.likes.add(user)
            is_liked = True
        response_data = {
            'is_liked': is_liked,
            'likes_count': post.number_of_likes(),
        }
        
        return JsonResponse(response_data)
    