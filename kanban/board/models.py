import datetime
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'({self.id}) {self.title}'

class Contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mail = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

