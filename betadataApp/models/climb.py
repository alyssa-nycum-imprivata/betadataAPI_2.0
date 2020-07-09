from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .gym import Gym

class Climb(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gym = models.OneToOneField(Gym, on_delete=models.CASCADE)
    climb_type = models.CharField(max_length=20)
    grade = models.IntegerField()
    description = models.CharField(max_length=300)
    beta_comments = models.CharField(max_length=500)
    rating = models.IntegerField()
    created_on = models.DateTimeField()
    is_archived = models.BooleanField()

    def __str__(self):
        return f'{self.grade} - {self.description}'

    class Meta:
        ordering = (F('self.created_on').desc(nulls_last=True),)