from django.contrib import admin
from .models import Artist, Canvas, Design, Artwork

# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'sku_code',
        'name',
        'full_name',
    )

    ordering = ('friendly_name',)


class CanvasAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'sku_code',
        'name',
        'price',
    )

    ordering = ('friendly_name',)


class DesignAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'sku_code',
        'name',
        'artist',
    )

    ordering = ('friendly_name',)


class ArtworkAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'friendly_name',
        'name',
        'artist',
        'design',
        'canvas',
    )

    ordering = ('sku',)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Canvas, CanvasAdmin)
admin.site.register(Design, DesignAdmin)
admin.site.register(Artwork, ArtworkAdmin)
