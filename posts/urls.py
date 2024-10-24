from django.urls import path
from .views import posts, delete_post

urlpatterns = [
    path('', posts, name='posts'),
    path('delete/<int:id>/', delete_post, name='delete_post')
]