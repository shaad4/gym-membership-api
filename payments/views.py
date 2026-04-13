from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Payment
from .serializers import PaymentSerializer
# Create your views here.

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == 'owner':
            return Payment.objects.filter(membership__gym__owner=user)
        
        return Payment.objects.filter(user=user)
    
    def perform_create(self, serializer):
        membership = serializer.validated_data['membership']

        existing = Payment.objects.filter(
            user=self.request.user,
            membership = membership,
            status = 'success'
        )

        if existing.exists():
            raise PermissionDenied("You already purchase this membership")

        amount = membership.price
        serializer.save(
            user=self.request.user,
            amount=amount,
            status='success'
        )