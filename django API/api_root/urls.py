
from django.contrib import admin
from django.urls import path
from api_rest.views import UserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', UserView.as_view()),
    path('users/<int:pk>/', UserView.as_view()),
]
