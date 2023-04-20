from django.shortcuts import render
from rest_framework import generics, viewsets
from django.contrib.auth import get_user_model
from rest_framework.permissions import *
from .permissions import IsOwner
from .serializers import UserSerializer, UpdateUserSerializer

User = get_user_model()

class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_by_action = {
        'list': [IsAuthenticatedOrReadOnly],
        'create': [AllowAny],
        'retrieve': [IsAuthenticatedOrReadOnly],
        'update': [IsOwner | IsAdminUser],
        'delete': [IsOwner | IsAdminUser],
    }

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
        

class UpdateDataAPIView(generics.UpdateAPIView,
                        generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [IsOwner | IsAdminUser]
