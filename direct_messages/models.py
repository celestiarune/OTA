from django.db import models
from common.models import CommonModel
from django.conf import settings


class ChattingRoom(CommonModel):

    """Room model definition"""

    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="chattingrooms")

    def __str__(self) -> str:
        return "Chatting Room."

class Message(CommonModel):

    """Message model definition"""

    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="messages",)
    room = models.ForeignKey("direct_messages.ChattingRoom", on_delete=models.CASCADE, related_name="messages",)

    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"