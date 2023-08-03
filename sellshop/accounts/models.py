from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
         
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # if not email:
        #     raise ValueError('The email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)

TITLE_CHOICES = [
    ('mr', 'Mr'),
    ('mrs', 'Mrs')
]

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=100)
    social_title = models.CharField(choices=TITLE_CHOICES, blank=True, null=True, max_length=5)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateField(blank=True, null=True)
    newsletter = models.BooleanField(default=True)
    offers = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
class Address(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    town_city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    additional_info = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')