from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

class Gym(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = (F('self.name').asc(nulls_last=True),)