from django.urls import path
from .views import home, login_view, signup_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login_view'),
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view')
]