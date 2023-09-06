from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from rooms.models import Room
from experiences.models import Experience

class User(AbstractUser):
    
    class GenderChoices(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    class LanguageChoices(models.TextChoices):
        KR = "kr", "Korean"
        EN = "en", "English"

    class CurrencyChoices(models.TextChoices):
        KRW = "krw", "Korean Won"
        USD = "usd", "USA Dollar"

    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    
    avatar = models.ImageField(blank=True)
    name = models.CharField(max_length=150, default="")
    is_host = models.BooleanField(null=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices)

    @receiver(post_save, sender=Room)
    @receiver(post_save, sender=Experience)
    @receiver(post_delete, sender=Room)
    @receiver(post_delete, sender=Experience)
    def set_is_host(sender, instance, **kwargs):
        if instance.owner:
            # Check if the user has any rooms or experiences
            has_rooms = Room.objects.filter(owner=instance.owner).exists()
            has_experiences = Experience.objects.filter(owner=instance.owner).exists()

            # Calculate the new is_host value
            is_host = has_rooms or has_experiences

            # Update is_host only for the specific user
            instance.owner.is_host = is_host

            # Use F() objects to update the is_host field without fetching the entire user object
            User.objects.filter(pk=instance.owner.pk).update(is_host=is_host)