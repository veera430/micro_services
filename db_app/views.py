from rest_framework import viewsets
from .models import UserDetails
from .serializers import UserDetailsSerializer

class UserDetails_viewset(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer
