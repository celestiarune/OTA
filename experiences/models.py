from django.db import models
from common.models import CommonModel
from django.conf import settings


class Experience(CommonModel):

    """Experiences Model Definition"""

    country = models.CharField(max_length=50, default="US")
    city = models.CharField(max_length=80, default="New York")
    name = models.CharField(max_length=250)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="experiences",)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start = models.TimeField()
    end = models.TimeField()
    description = models.TextField()

    perks = models.ManyToManyField("experiences.Perk", related_name="experiences",)
    category = models.ForeignKey("categories.Category", null=True, blank=True, on_delete=models.SET_NULL, related_name="experiences",)


    def __str__(self) -> str:
        return self.name



class Perk(CommonModel):

    """What is included on an Experience"""

    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=250, blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    

