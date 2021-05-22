from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.IntegerField()



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.TextField()
    carno = models.TextField()
    optype = models.TextField()


class Point(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    speed = models.IntegerField()
    interventions = models.IntegerField()
    speeding = models.IntegerField()



