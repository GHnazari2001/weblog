from django.urls import path
from .views import SignUpView,profileView,UpdateProfieView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', profileView.as_view(), name='profile'),
    path('profile/edit/', UpdateProfieView.as_view(), name='profile_edit'),
]
