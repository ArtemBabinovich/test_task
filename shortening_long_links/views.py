from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from configuration.settings import ALLOWED_HOSTS
from shortening_long_links.forms import UserRegisterForm, UrlForm
from shortening_long_links.models import Links


def error(request, exception):
    return render(request, 'error/404.html', status=404)


class UserLoginView(LoginView):
    """Класс авторизации пользователя на сайте"""
    template_name = "shortening_long_links/accounts/login.html"


class UserLogoutView(LogoutView):
    """Класс для выхода пользователя с аккаунта"""
    template_name = "shortening_long_links/accounts/logout.html"


@login_required
def profile(request):
    """Функция для отображения профиля авторизованного пользователя"""
    url = Links.objects.filter(user=request.user).order_by("-id")
    return render(request, 'shortening_long_links/accounts/profile.html', {'url': url})


class RegisterUserView(CreateView):
    """Класс, регистрирующий пользователя на сайте"""
    model = User
    form_class = UserRegisterForm
    template_name = "shortening_long_links/accounts/registration.html"
    success_url = reverse_lazy('register_done')


@login_required
def add_url(request):
    """Функция добавление URL"""
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            links = form.save(commit=False)
            links.user = request.user
            links.save()
            return redirect(done_add)
    else:
        form = UrlForm
    return render(request, 'shortening_long_links/add_links.html', {'form': form})


@login_required
def done_add(request):
    """Функция отображения последнего преобразованного URL"""
    url = Links.objects.filter(user=request.user).last()
    return render(request, 'shortening_long_links/done_add.html', {'url': url})


class RegisterDoneView(TemplateView):
    template_name = 'shortening_long_links/accounts/registration_done.html'


def redirect_url(request, slug):
    url = ALLOWED_HOSTS[0]
    sl = f'{url}' + '/' + slug
    target = get_object_or_404(Links, slug=sl)

    return HttpResponseRedirect(target.links)
