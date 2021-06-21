from django.urls import path

from users.views import UserAuthorizationLoginView, UserLogoutLogoutView, \
    UserRegistrationCreateView, UserProfileUpdateView

app_name = 'users'

urlpatterns = [
    path('login/', UserAuthorizationLoginView.as_view(), name='login'),
    path('register/', UserRegistrationCreateView.as_view(), name='register'),
    path('profile/<int:pk>/', UserProfileUpdateView.as_view(), name='profile'),
    path('logout/', UserLogoutLogoutView.as_view(), name='logout'),

]
