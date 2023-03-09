from django.contrib import admin
from .models import Artist, Canvas, Design, Artwork

# Register your models here.
admin.site.register(Artist)
admin.site.register(Canvas)
admin.site.register(Design)
admin.site.register(Artwork)
