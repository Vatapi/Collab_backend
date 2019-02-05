from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    choices_project = (
        ('completed' , 'Completed'),
        ('collab' , "Looking for Collaboration")
    )
    title = models.CharField(max_length = 100)
    description = models.TextField()
    status = models.CharField(max_length = 10, choices = choices_project)
    skills = models.TextField()
    user_posted = models.ForeignKey(to=User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title
