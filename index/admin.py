from django.contrib import admin
from .models import Collection, Place, CollectionShots, Video, PlaceShots
from django.utils.safestring import mark_safe


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(CollectionShots)
class CollectionShotsAdmin(admin.ModelAdmin):
    list_display = ("collection", "get_image")

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='50' height='30'")


class CollectionShotsInline(admin.TabularInline):
    model = CollectionShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='150' height='110'")


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("place", "name")
    inlines = [CollectionShotsInline]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("place", "event")


@admin.register(PlaceShots)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("place", "get_image")

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='100' height='60'")