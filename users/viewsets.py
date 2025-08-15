from rest_framework import viewsets,mixins
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import IsProfileOwnerOrGetPost, IsUserOwnerGetPost

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes =[IsUserOwnerGetPost,]
    
class ProfileViewSet(viewsets.ModelViewSet,mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes =[IsProfileOwnerOrGetPost,]
    # authentication 