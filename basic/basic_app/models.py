from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    # This OneToOneField(User) is importd from django.contrib.auth.models and not the above Class User
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.URLField(blank=True)
    picture = models.ImageField(
        upload_to='basic_app/profile_pics', blank=True)

    def __str__(self):
        return self.user.username
