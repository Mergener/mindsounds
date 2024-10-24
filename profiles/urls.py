from django.urls import path
from .views import profile_view, profile_search_results_view, follow

urlpatterns = [
    path('<str:username>/', profile_view, name='profile_view'),
    path('search/<str:query>/', profile_search_results_view, name='profile_search_results_view'),
    path('follow/<str:username>/', follow, name='follow')
]