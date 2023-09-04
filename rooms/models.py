from django.db import models
from django.conf import settings
from common.models import CommonModel

class Room(CommonModel):

    """ Room Model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=180, default="")
    country = models.CharField(max_length=50, default="US")
    city = models.CharField(max_length=80, default="New York")
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amenities = models.ManyToManyField("rooms.Amenity")
    category = models.ForeignKey("categories.Category", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.name
    
    def total_amenities(self):
        return self.amenities.count()


class Amenity(CommonModel):
    
    """Amenity Definition"""
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"