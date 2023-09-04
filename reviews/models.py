from django.db import models
from common.models import CommonModel
from django.conf import settings

class Review(CommonModel):
    
    """Review from a user to a Room or Experience"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", null=True, blank=True, on_delete=models.SET_NULL)
    experience = models.ForeignKey("experiences.Experience", null=True, blank=True, on_delete=models.SET_NULL)
    payload = models.TextField()
    rating = models.PositiveIntegerField()


    def __str__(self) -> str:
        return f"{self.user} / {self.rating}★"
