from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser):
    team_leader = models.BooleanField()
    assigned = models.BooleanField(default=False)

    objects = CustomUserManager()
    REQUIRED_FIELDS = ['team_leader', 'email']


class team(models.Model):
    team_name = models.CharField(max_length=100, default=None)
    members = models.ManyToManyField(CustomUser,  related_name= 'team_members')

    def __str__(self):
        return self.team_name

class task(models.Model):
    task_name = models.CharField(max_length=100)
    priority = models.BooleanField()
    start_date = models.DateField()
    end_date = models.DateField()
    team_member = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    assigned = models.BooleanField()
    in_progress = models.BooleanField()
    under_review = models.BooleanField()
    done = models.BooleanField()

    def __str__(self):
        return self.task_name


class Report(models.Model):
    date = models.DateField()
