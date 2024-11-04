# inventory/admin.py

from django.contrib import admin
from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Book model.
    """
    list_display = ('title', 'author', 'genre', 'publication_date', 'isbn')
    search_fields = ('title', 'author', 'genre', 'publication_date')
