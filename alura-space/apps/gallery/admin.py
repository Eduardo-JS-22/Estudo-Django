from django.contrib import admin
from apps.gallery.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'legend', 'category', 'published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'legend', 'category')
    list_filter = ('id', 'name', 'category', 'published')
    list_per_page = 25
    list_editable = ('published',)

admin.site.register(Image, ImageAdmin)