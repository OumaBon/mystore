from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


    def __str__(self) -> str:
        return f'{self.name}'


class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self) -> str:
        return f"{self.user.username}- {self.role.name if self.role else "No role"}"
