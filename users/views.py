from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from baskets.models import Basket
from users.models import User


class UserAuthorizationLoginView(LoginView):
    """
    Страница авторизации
    setting.py -> LOGIN_REDIRECT_URL = '/products/'
    """
    template_name = 'users/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super(UserAuthorizationLoginView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Авторизация',
        })
        return context

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        messages.success(self.request, "Авторизация прошла успешно")
        return HttpResponseRedirect(self.get_success_url())


class UserRegistrationCreateView(CreateView):
    """Страница регистрации нового пользователя"""
    model = User
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    form_class = UserRegisterForm

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationCreateView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Регистрация',
        })
        return context

    def form_valid(self, form):
        super().form_valid(form)
        messages.success(self.request, "Пользователь успешно создан. Авторизуйтесь")
        return HttpResponseRedirect(self.get_success_url())


class UserProfileUpdateView(UpdateView):
    """Страница профиля"""
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileUpdateView, self).get_context_data(**kwargs)
        context.update({
            'title': 'Редактирование профиля',
            'baskets': Basket.objects.filter(user=self.request.user),
        })
        return context

    def form_valid(self, form):
        # Работает криво (позволяет писать всякую чушь и сохранять)
        super().form_valid(form)
        messages.success(self.request, "Изменения сохранены")
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # self.success_url или success_url ?????????
        success_url = reverse_lazy('users:profile', kwargs={'pk': self.object.pk})
        return success_url

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserProfileUpdateView, self).dispatch(request, **kwargs)


class UserLogoutLogoutView(LogoutView):
    """ 2 варианта:
    1) next_page = '/'
    2) в settings.py написать LOGOUT_REDIRECT_URL = '/' , а в классе - pass
    """
    pass
