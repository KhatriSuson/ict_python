from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Level(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.IntegerField(default=1)

    def __str__(self):
        return self.name
    
class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    code_stub = models.TextField()  # Starting code
    solution = models.TextField()   # Correct solution code
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)