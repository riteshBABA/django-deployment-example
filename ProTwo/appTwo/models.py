from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    fname = models.CharField(max_length = 254)
    lname = models.CharField(max_length = 254)
    email = models.EmailField(unique = True, max_length=254)

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #adding more attributes to user
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
