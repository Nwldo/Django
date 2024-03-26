from django.contrib import admin
from django.urls import path
from apirest.views import RegisterListAPIView, RegisterUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registers/', RegisterListAPIView.as_view(), name='user-list-create'),
    path('registers/<int:pk>/', RegisterUpdateAPIView.as_view(), name='user-update-destroy'),
]
