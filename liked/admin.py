from django.contrib import admin
from liked.models import LikedItem
from django.utils.html import format_html
from django.urls import reverse


@admin.register(LikedItem)
class LikedItemAdmin(admin.ModelAdmin):
    list_display = ["_id", "user_id", "content_object"]

    def user_id(self, likedItem: LikedItem):
        url = reverse("admin:core_user_changelist")
        return format_html("<a href={}>{}</a>", url, likedItem.user_id)
