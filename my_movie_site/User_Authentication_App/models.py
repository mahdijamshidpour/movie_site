from django.db import models
from django.contrib.auth.models import User

class UserProfileExtraInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_mobnumber = models.IntegerField(blank=True)
    profile_pic = models.ImageField(upload_to='User_Authentication_App/profile_pics',blank=True)

    def __str__(self):
        return self.user.username
