from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

class Goal(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goal_content = models.CharField(max_length=500)
    complete_by = models.DateField()
    is_complete = models.BooleanField()
    completed_on = models.DateField()
    
    def __str__(self):
        return self.goal_content

    class Meta:
        ordering = (F('self.complete_by').desc(nulls_last=True),)