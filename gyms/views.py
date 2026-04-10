from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Gym, Membership
from .serializers import GymSerializer, MembershipSerializer
from .permissions import IsOwner

# Create your views here.

class GymViewSet(ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Gym.objects.filter(owner = self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class MembershipViewSet(ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Membership.objects.filter(gym__owner = self.request.user)

    def perform_create(self, serializer):
        gym = serializer.validated_data['gym']

        if gym.owner != self.request.user:
            raise PermissionDenied("You can only add plans to your own gym")

        serializer.save()