from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import ContactSerializer, TaskSerializer
from .models import Contact, Task
from rest_framework.views import APIView

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('created_at')
    serializer_class = TaskSerializer
    permission_classes = [] #permissions.IsAuthenticated

class ContactView(APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = []

    def get(self, request, format=None):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)