from rest_framework.response import Response
from rest_framework import viewsets
from api.models import Todo
from api.serializers import TodoSerializer



class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
