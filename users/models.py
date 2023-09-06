from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
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


@receiver([post_save, post_delete], sender=Experience)
def update_user_is_host_on_experience_change(sender, instance, **kwargs):
    user = instance.owner
    if user:
        has_rooms = Room.objects.filter(owner=user).exists()
        has_experiences = Experience.objects.filter(owner=user).exists()
        is_host = has_rooms or has_experiences
        user.is_host = is_host
        user.save()

@receiver([post_save, post_delete], sender=Room)
def update_user_is_host_on_room_change(sender, instance, **kwargs):
    user = instance.owner
    if user:
        has_rooms = Room.objects.filter(owner=user).exists()
        has_experiences = Experience.objects.filter(owner=user).exists()
        is_host = has_rooms or has_experiences
        user.is_host = is_host
        user.save()