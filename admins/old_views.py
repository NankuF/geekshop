# @user_passes_test(lambda u: u.is_superuser)
# def admin_users(request):
#     context = {'title': ' Админ | Пользователи', 'users': User.objects.all()}
#     return render(request, 'admins/admin-users-read.html', context)

# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminRegisterForm()
#     context = {'title': 'Админ | Регистрация', 'form': form}
#     return render(request, 'admins/admin-users-create.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_update(request, id):
#     selected_user = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=selected_user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admins:admin_users'))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#         context = {
#             'title': 'Админ | Обновление пользователя',
#             'form': form,
#             'selected_user': selected_user,
#         }
#         return render(request, 'admins/admin-users-update-delete.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def admin_users_delete(request, id):
#     user = User.objects.get(id=id)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:admin_users'))