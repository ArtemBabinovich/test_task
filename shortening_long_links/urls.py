from django.urls import path
from .views import UserLoginView, UserLogoutView, profile, RegisterUserView, add_url, done_add, RegisterDoneView, \
    redirect_url

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('register/done', RegisterDoneView.as_view(), name='register_done'),
    path('add_url/', add_url, name='add_url'),
    path('done_url/', done_add, name='done_add'),
    path('<str:slug>', redirect_url, name='redirect_url'),
]
