from typing import Any, List, Optional, Tuple
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class WordFilter(admin.SimpleListFilter):

    title = "Filter by Words"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, queryset):
        word = self.value()
        return queryset.filter(payload__contains=word) if word else queryset


class ReviewQualityFilter(admin.SimpleListFilter):

    title = "Filter by Good or Bad"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]
    
    def queryset(self, request, queryset):
        word = self.value()
        if word == "good":
            return queryset.filter(rating__gte=3)
        elif word == "bad":
            return queryset.filter(rating__lt=3)
        else:
            return queryset





@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    
    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        ReviewQualityFilter,
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )