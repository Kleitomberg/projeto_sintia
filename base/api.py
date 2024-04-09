from django.urls import path  # type: ignore

from users.views import LoginView, UserCreate, UserListView, UserRetrieveUpdateDestroy

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', UserCreate.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='users'),
    path('users/<int:id>', UserRetrieveUpdateDestroy.as_view(), name='users-detail'),
]
