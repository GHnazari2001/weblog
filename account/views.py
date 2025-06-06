from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    

class profileView(LoginRequiredMixin,DetailView):
    model=CustomUser
    template_name = 'profile.html'
    context_object_name ='user_profile'
    
    def get_object(self, queryset = None):
        return self.request.user

class UpdateProfieView(LoginRequiredMixin,UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'profile_form.html'
    success_url =reverse_lazy('profile')
    def get_object(self, queryset = None):
        return self.request.user