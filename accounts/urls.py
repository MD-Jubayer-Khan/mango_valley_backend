from django.urls import path
from .views import UserDetailView, UserListView

urlpatterns = [
    path('user/', UserDetailView.as_view(), name='user-detail'),
    path('users/', UserListView.as_view(), name='user-list'),
]