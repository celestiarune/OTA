from django.db import models
from common.models import CommonModel
from django.conf import settings


class Booking(CommonModel):

    """Booking model definition"""
    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "Room"
        EXPERIENCE = "experience", "Experience"

    kind = models.CharField(max_length=15, choices=BookingKindChoices.choices)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", null=True, blank=True, on_delete=models.SET_NULL)
    experience = models.ForeignKey("experiences.Experience", null=True, blank=True, on_delete=models.SET_NULL)
    check_in = models.DateField(null=True, blank=True)
    check_out = models.DateField(null=True, blank=True)
    experience_time = models.DateTimeField(null=True, blank=True)
    guests = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.kind.title()} booking for: {self.user}"