import datetime
from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=[
        ('todo', 'Todo'),
        ('inProgress', 'In Progress'),
        ('awaitFeedback', 'Await Feedback'),
        ('done', 'Done')
    ], default='todo')
    priority = models.CharField(max_length=6, choices=[
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ], default='medium')
    due_date = models.DateField(default=datetime.date.today)
    assigned_to = models.ManyToManyField('Contact', related_name='assigned_tasks')
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title
