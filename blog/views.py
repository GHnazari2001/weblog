

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View,TemplateView
)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse, HttpResponseForbidden
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q

from .models import Post, Category
from .forms import PostForm, CommentForm
from taggit.models import Tag
from account.models import CustomUser


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post_list'
    paginate_by = 3

    def get_queryset(self):
       
        return Post.objects.select_related('author', 'category').prefetch_related('tags').order_by('-date')

class AboutView(TemplateView):
    template_name = "about.html"

class ContactView(TemplateView):
    template_name = "contact.html"
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        # اضافه کردن فرم دیدگاه به context
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        
        post = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
        else:
            # اگر فرم نامعتبر بود، صفحه را با فرم و خطاهایش نمایش بده
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)


class PostNewView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

    def test_func(self):
        # کاربر فقط در صورتی می‌تواند پست را ویرایش کند که نویسنده آن باشد
        obj = self.get_object()
        return obj.author == self.request.user
   


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class LikePostView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        
        is_liked = post.likes.filter(id=user.id).exists()

        if is_liked:
            post.likes.remove(user)
        else:
            post.likes.add(user)

        return JsonResponse({
            'is_liked': not is_liked,
            'likes_count': post.number_of_likes(),
        })


class AuthorPostListView(ListView):
    model = Post
    template_name = 'author_posts.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        # گرفتن نویسنده از URL و فیلتر کردن پست‌ها
        self.author = get_object_or_404(CustomUser, username=self.kwargs['username'])
        
        return Post.objects.filter(author=self.author).select_related('author', 'category').prefetch_related('tags').order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context


class TaggedPostListView(ListView):
    model = Post
    template_name = 'posts_by_tag.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
    
        return Post.objects.filter(tags__in=[self.tag]).select_related('author', 'category').prefetch_related('tags').order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.tag.name
        return context


class CategoryPostListView(ListView):
    model = Post
    template_name = 'category_posts.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        
        return Post.objects.filter(category=self.category).select_related('author', 'category').prefetch_related('tags').order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class SearchView(ListView):
    model = Post
    template_name = 'search_result.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # بهینه‌سازی
            return Post.objects.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            ).select_related('author', 'category').prefetch_related('tags').order_by('-date')
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context