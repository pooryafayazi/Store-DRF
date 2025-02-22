from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils.translation import gettext_lazy as _ # This is used to translate the string to the user's language
from django.db.models.signals import post_save
from django.dispatch import receiver

from .validators import validate_phone_number

class UserType(models.IntegerChoices):
    costumer = 1 , _('costumer')
    admin = 2 , _('admin')
    superuser = 3 , _('superuser')



class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('type', UserType.superuser.value)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=True)    
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    type = models.IntegerField(choices=UserType.choices, default=UserType.costumer.value)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    def __str__(self):
        return self.email


class UsedResetToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user_id = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return self.token
    

class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12, null=True, blank=True, validators=[validate_phone_number])
    image = models.ImageField(blank=True , null=True)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email
    
    
@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created and instance.type == UserType.costumer.value:
        Profile.objects.create(user=instance, pk=instance.pk)

