from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User ,on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    def __str__(self):
        return f"Profile {self.user.username}"