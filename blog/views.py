from django.shortcuts import render,get_object_or_404
from django.views.generic import View ,CreateView,DetailView,FormView,ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post,Category
from .forms import PostForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.core.paginator import Paginator
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin 
# Create your views here.

class HomeView(View):
    #model = Post
    template_name = 'home.html'
    paginate_by = 2
    
    def get(self ,request):
        posts = Post.objects.all()
        paginator = Paginator(posts ,self.paginate_by)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
       
        return render(request ,self.template_name , {'post_list': page_obj})
    
    
    
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

    
    
class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'excerpt', 'body','photo']
    


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

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
            ).order_by('-date').distinct() # distinct برای جلوگیری از نتایج تکراری اگر join دارید
        else:
            # اگر عبارتی برای جستجو وارد نشده یا query خالی است، یک QuerySet خالی برگردان
            queryset = Post.objects.none()
            
        return queryset # این return باید همیشه یک QuerySet برگرداند

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '') # ارسال عبارت جستجو به تمپلیت
        return context
    
class CategoryPostListView(ListView):
    model = Post # ما می‌خواهیم لیستی از آبجکت‌های Post را نمایش دهیم
    template_name = 'category_posts.html' # مسیر تمپلیتی که در مرحله بعد ایجاد می‌کنیم
    context_object_name = 'post_list' # نام متغیری که در تمپلیت برای لیست پست‌ها استفاده می‌شود
    paginate_by = 2 # تعداد پست‌ها در هر صفحه (اختیاری)

    def get_queryset(self):

        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        queryset = Post.objects.filter(category=self.category).order_by('-date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
      
        context['category'] = self.category
        return context
