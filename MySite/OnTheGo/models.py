from django.db import models
import django_tables2 as tables

from . import choices

# Create your models here.
class ServiceUser(models.Model):
    user = models.CharField(max_length=100)
    support_worker = models.CharField(max_length=100)
    level_of_support = models.IntegerField(choices.SUPPORT_LEVEL)
    last_contact_time = models.DateTimeField()
    last_contact_place = models.CharField(max_length=200)
    goals_achieved = models.IntegerField()
    age = models.IntegerField(22)
    total_goals = models.IntegerField(10)
