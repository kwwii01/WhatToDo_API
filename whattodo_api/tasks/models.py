from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    """Model that represents status of a task"""
    name = models.fields.CharField(max_length=24)

    class Meta:
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name


class Priority(models.Model):
    """Model that represents priority of a task"""
    name = models.fields.CharField(max_length=24)

    class Meta:
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name


class Task(models.Model):
    """Model that represents tasks"""
    summary = models.CharField(max_length=128)
    detailed_description = models.TextField()
    definition_of_done = models.CharField(max_length=128)
    creation_date = models.DateTimeField(auto_now=True)

    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    priority = models.ForeignKey(Priority, null=True, on_delete=models.SET_NULL)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
