from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.role = 'staff'  # default role
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.create_user(username, email=email, password=password, **extra_fields)
        user.role = 'admin'
        user.save(using=self._db)
        return user

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class FileData(models.Model):
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    views = models.CharField(max_length=128)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_sq_ft = models.DecimalField(max_digits=10, decimal_places=2)
    rate_per_sq_ft = models.DecimalField(max_digits=10, decimal_places=2)
    unit_no = models.CharField(max_length=100)

    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uploaded_data")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.unit_no} - {self.category}"