from django.db import models

# Create your models here.

class Gym(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Membership(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE, related_name='memberships')
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.gym.name}"
    

    