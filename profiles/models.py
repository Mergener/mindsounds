from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True) 
    join_date = models.DateTimeField(auto_now_add=True)


class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return f'{self.follower} follows {self.user}'

admin.site.register(Profile)
admin.site.register(Follower)