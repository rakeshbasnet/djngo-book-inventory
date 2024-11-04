from django import forms
from .models import Inventory


# BookForm is a form based on the Book model for adding new books to the inventory
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory  # Links the form to the Book model
        fields = ['title', 'author', 'genre', 'publication_date', 'isbn']  # Specifies fields to include in the form
