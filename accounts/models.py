from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    course = models.CharField(max_length=20)

    def __str__(self):
        return str(self.user)
