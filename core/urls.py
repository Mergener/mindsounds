from django.urls import path
from .views import base_view, login_view

urlpatterns = [
    path('', base_view, name='base_view'),
    path('login/', login_view, name='login_view')
]