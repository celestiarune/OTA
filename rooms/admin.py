from django.contrib import admin
from .models import Room, Amenity

@admin.action(description="Set all prices to zero")
def reset_prices(model_admin, request, room):
    room.update(price=0)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
        "updated_at",
    )



    list_filter = (
        "name",
        "country",
        "city",
        "price",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )
    search_fields = (
        # "name",
        # "price",
        "^owner__username",
    )



@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )