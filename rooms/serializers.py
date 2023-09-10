from rest_framework.serializers import ModelSerializer
from .models import Room, Amenity
from users.siralizers import TinyUserSerializer

class AmenitySerializer(ModelSerializer):
    
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


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

    owner = TinyUserSerializer()
    amenities = AmenitySerializer(many=True)

    class Meta:
        model = Room
        fields = "__all__"
        

