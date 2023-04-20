from django.urls import path
from .views import ListToDoAPIView ,ToDoDetailGenerics, TodoAPIView

urlpatterns = [
    path('todo/', TodoAPIView.as_view(), name='todoapi'),
    path('todo/<int:pk>', ListToDoAPIView.as_view(), name='todo'),
    path('todo/detail/<int:pk>/', ToDoDetailGenerics.as_view(), name='todo_create'),
]

