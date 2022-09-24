from django.contrib import admin
from liked.models import LikedItem


@admin.register(LikedItem)
class LikedItemAdmin(admin.ModelAdmin):
    list_display = ["_id", "user_id", "content_object"]
