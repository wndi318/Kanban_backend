from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Contact, Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'created_at']

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email']