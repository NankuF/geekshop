# from django.shortcuts import HttpResponseRedirect, render
# from django.contrib import messages, auth
# from django.urls import reverse
# from django.contrib.auth.decorators import login_required
#
# from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
# from baskets.models import Basket
#
#
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
#
#
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
#
#
# @login_required
# def profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Изменения сохранены')
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=user)
#
#     # Вариант расчета total_quantity и total_sum
#     # baskets = Basket.objects.filter(user=user)
#     # total_quantity = 0
#     # total_sum = 0
#     # for basket in baskets:
#     #     total_quantity += basket.quantity
#     #     total_sum += basket.sum()
#     #
#     # Рефакторинг
#     # total_quantity = sum(basket.quantity for basket in baskets)
#     # total_sum = sum((basket.product.price * basket.quantity) for basket in baskets)
#
#     context = {
#         'title': 'GeekShop - Личный кабинет',
#         'form': form,
#         'baskets': Basket.objects.filter(user=user),
#         # 'baskets': baskets,
#         # 'total_quantity': total_quantity,
#         # 'total_sum': total_sum,
#     }
#     return render(request, 'users/profile.html', context)
#
#
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))
