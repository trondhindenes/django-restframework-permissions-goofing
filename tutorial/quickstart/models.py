from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db.models import Model
from rules.contrib.models import RulesModelBase, RulesModelMixin


class TaskGroup(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    owned_by_group = models.ForeignKey(Group, on_delete=models.CASCADE)

    # class Meta:
    #     permissions = (("assign_tasks", "Assign task"),)


class Task(models.Model):
    summary = models.CharField(max_length=32)
    content = models.TextField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    task_group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE)

