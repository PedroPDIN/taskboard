from django.shortcuts import render
from .models import Board, Task
from .serializer import BoardSerializer, TaskSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action


def index(request):
    context = {
      'minha_chave': Board.objects.all() 
      }

    return render(request, 'index.html', context)


class BoardViewSets(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class TaskViewSets(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=False) # uma ação extra | essa é uma outra ação que não vai entra nos detalhes
    def pending(self, request):
        queryset = Task.objects.all().filter(status="Pending")
        serializer = TaskSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False)
    def doing(self, request):
        queryset = Task.objects.all().filter(status="Doing")
        serializer = TaskSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)


    @action(detail=False)
    def done(self, request):
        queryset = Task.objects.all().filter(status="Done")
        serializer = TaskSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
