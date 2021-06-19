from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth import views, login as auth_login
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView

from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from baskets.models import Basket
from users.models import User


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {'title': 'Authorization', 'form': form}
#     return render(request, 'users/login.html', context)


class UserAuthorizationLoginView(views.LoginView):
    model = User
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')
    form_class = UserLoginForm

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        messages.success(self.request, "Авторизация прошла успешно")
        return HttpResponseRedirect(self.get_success_url())


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegisterForm()
#     context = {'title': 'Register', 'form': form}
#     return render(request, 'users/register.html', context)


class UserRegistrationCreateView(CreateView):
    model = User
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    form_class = UserRegisterForm

    def form_valid(self, form):
        super().form_valid(form)
        messages.success(self.request, "Пользователь успешно создан. Авторизуйтесь")
        return HttpResponseRedirect(self.get_success_url())


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения выполнены успешно')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)

    # Вариант расчета total_quantity и total_sum
    # baskets = Basket.objects.filter(user=user)
    # total_quantity = 0
    # total_sum = 0
    # for basket in baskets:
    #     total_quantity += basket.quantity
    #     total_sum += basket.sum()
    #
    # Рефакторинг
    # total_quantity = sum(basket.quantity for basket in baskets)
    # total_sum = sum((basket.product.price * basket.quantity) for basket in baskets)

    context = {
        'title': 'GeekShop - Личный кабинет',
        'form': form,
        'baskets': Basket.objects.filter(user=user),
        # 'baskets': baskets,
        # 'total_quantity': total_quantity,
        # 'total_sum': total_sum,
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
