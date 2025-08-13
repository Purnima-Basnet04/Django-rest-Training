from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from .permissions import*
from django_filters import filters

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsTaskOwnerOrReadOnly]
    filter_backends = [filters.orderingFilter]
    ordering_fields = ['title','created_at','updated_at']
    filterset_fields = ['status']