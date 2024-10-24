from django.urls import path
from .views import profile_view, profile_search_results_view, follow, unfollow, following_view, followers_view, update_bio_view

urlpatterns = [
    path('unfollow/<str:username>/', unfollow, name='unfollow'),
    path('followers/<str:username>/', followers_view, name='followers_view'),
    path('following/<str:username>/', following_view, name='following_view'),
    path('follow/<str:username>/', follow, name='follow'),
    path('search/', profile_search_results_view, name='profile_search_results_view'),
    path('<str:username>/update_bio', update_bio_view, name='update_bio_view'),
    path('<str:username>/', profile_view, name='profile_view'),
]