from django.urls import path
from .views import api_login

urlpatterns = [
    path('api/login/', api_login),
    path('create-admin/', create_admin),
]