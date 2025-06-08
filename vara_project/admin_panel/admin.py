from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'status', 'bedrooms', 'bathrooms', 'area_sqft', 'date_added')
    list_filter = ('status', 'bedrooms', 'bathrooms')
    search_fields = ('title', 'address', 'description')
    # For ImageField, you might want a custom display in admin, but this is fine for now.
