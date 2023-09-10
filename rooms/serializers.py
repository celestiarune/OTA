from rest_framework.serializers import ModelSerializer
from .models import Room, Amenity


class RoomListSerializer(ModelSerializer):

    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
        )

class RoomDetailSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        depth = 1

class AmenitySerializer(ModelSerializer):
    
    class Meta:
        model = Amenity
        fields = "__all__"