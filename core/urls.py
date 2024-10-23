from django.urls import path
from .views import base_view, login_view, signup_view, logout_view

urlpatterns = [
    path('', base_view, name='base_view'),
    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view')
]