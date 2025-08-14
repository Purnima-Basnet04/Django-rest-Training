from rest_framework import viewsets, response, status
from .models import Project
from .serializers import ProjectSerializer
from .permissions import*
from rest_framework.decorators import action


class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectOwnerOrReadOnly,]
    
    @action (detail=True, methods=['post'], name='join', permission_classes=[])
    def join(self, request, pk=None):
        try:
            project= self.get_object()
            user= request.user
            if not user in project.assigned_to.all():
                project.assigned_toadd(user)
                return response.Response({'message': "you have been assigned to this project"}, status=status.HTTP_202_ACCEPTED) 
            else:
                return response.Response({'message':" you are already assigned to this project"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return response.Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    