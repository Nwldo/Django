
from django.contrib import admin
from django.urls import path
from api_rest.views import UserListAPIView, UserUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserListAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserUpdateAPIView.as_view(), name='user-update-destroy'),
]