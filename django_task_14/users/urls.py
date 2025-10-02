from django.urls import path
from users.views import UserLoginView, UserLogoutView, UserDetailView, UserSignupView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
