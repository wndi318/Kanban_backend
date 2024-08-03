from django.shortcuts import render
from rest_framework import permissions, viewsets
from .serializers import ContactSerializer, TaskSerializer
from .models import Contact, Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('created_at')
    serializer_class = TaskSerializer
    permission_classes = [] #permissions.IsAuthenticated

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('firstname')
    serializer_class = ContactSerializer
    permission_classes = [] #permissions.IsAuthenticated
