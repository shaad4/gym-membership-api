from django.db import models

# Create your models here.

class Gym(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name