from django.shortcuts import render
from rest_framework import generics
from .models import ToDo
from .serializers import ListToDoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import  SearchFilter
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters


class TodoAPIView(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ListToDoSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['title','is_completed']
    search_fields = ['title']
    permission_classes = [IsAuthenticated]


class ListToDoAPIView(generics.ListCreateAPIView,
                      generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ListToDoSerializer
    permission_classes = [IsAuthenticated]


class ToDoDetailGenerics(generics.RetrieveAPIView,
                        generics.UpdateAPIView,
                        generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ListToDoSerializer
    permission_classes = [IsAuthenticated]



