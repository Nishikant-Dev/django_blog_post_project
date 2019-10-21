from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# as we are using default User Model, for having a profile picture for an User we will extend it with
# User model with one to one relationship
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
