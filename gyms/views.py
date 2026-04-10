from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.response import Response
from payments.models import Payment
from .models import Gym, Membership
from .serializers import GymSerializer, MembershipSerializer
from .permissions import IsOwner

# Create your views here.

class GymViewSet(ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and user.role == 'owner':
            return Gym.objects.filter(owner=user)
        
        return Gym.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    @action(detail=True, methods=['GET'])
    def user(self, request, pk=None):
        gym = self.get_object()

        if gym.onwer != request.user:
            raise PermissionDenied("Not Your Gym")
        
        payments = Payment.objects.filter(membership__gym=gym)

        users = []
        for p in payments:
            users.append({
                'id' : p.user.id,
                'username' : p.user.username
            })

        return Response(users)


class MembershipViewSet(ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        queryset = Membership.objects.all()

        gym_id = self.request.query_params.get('gym')
        if gym_id:
            queryset = queryset.filter(gym_id=gym_id)

        if user.is_authenticated and user.role == 'owner':
            return queryset.filter(gym__owner=user)
        
        return queryset


    def perform_create(self, serializer):
        if self.request.user.role != 'owner':
            raise PermissionDenied("Only owners can create membership")
        
        gym = serializer.validated_data['gym']

        if gym.owner != self.request.user:
            raise PermissionDenied("You can only add plans to your own gym")

        serializer.save()