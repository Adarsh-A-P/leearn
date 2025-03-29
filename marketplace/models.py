from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    year_of_study = models.CharField(max_length=1)
    academic_period = models.CharField(max_length=9)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    cv = models.FileField(upload_to='cvs/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
