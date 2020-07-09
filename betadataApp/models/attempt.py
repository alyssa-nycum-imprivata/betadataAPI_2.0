from django.db import models
from django.db.models import F
from .climb import Climb

class Attempt(models.Model):

    climb = models.OneToOneField(Climb, on_delete=models.CASCADE)
    attempt_date = models.DateField()
    number_of_falls = models.IntegerField()
    number_of_attempts = models.IntegerField()
    is_flashed = models.BooleanField()
    is_clean = models.BooleanField()
    created_on = models.DateTimeField()

    def __str__(self):
        return f'{self.grade} - {self.description}'

    class Meta:
        ordering = (F('self.created_on').desc(nulls_last=True),)