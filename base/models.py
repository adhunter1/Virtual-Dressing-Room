from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    #user= models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(
        get_user_model(), related_name="profile", on_delete=models.CASCADE
    )
    #image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    shoulders = models.CharField(
        verbose_name="shoulders",
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )
    bust = models.CharField(
        verbose_name="bust",
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )

    waist = models.CharField(
        verbose_name="waist",
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )
    hips = models.CharField(
        verbose_name="hips",
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )
    height = models.CharField(
        verbose_name="height",
        max_length=255,
        default=None,
        blank=True,
        null=True,
    )



    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **__):
    """Hook for creating profiles."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=get_user_model())
def save_user_profile(sender, instance, **__):
    """Hook for updating profiles."""
    instance.profile.save()

class Dresses(models.Model):
    #user  = models.OneToOneField(
     #   get_user_model(), on_delete=models.CASCADE
    #)
    
    name  = models.TextField(default="")
    image = models.ImageField(upload_to='images/')


    def __str__(self):
     #   return f'{self.user.username} Dresses'
        return self.name
