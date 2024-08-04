from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Contact, Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Task
        fields = ['id','title', 'description', 'users', 'status', 'priority', 'due_date']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'