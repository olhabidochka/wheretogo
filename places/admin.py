from django.contrib import admin
from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'place_type', 'rating', 'location', 'created_at']
    list_filter = ['place_type', 'rating', 'created_at']
    search_fields = ['name', 'description', 'location']
    ordering = ['-created_at']
