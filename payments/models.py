from django.db import models

# Create your models here.


class Payment(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    )

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    membership = models.ForeignKey('gyms.Membership', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='pending')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.status}"