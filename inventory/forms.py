from django import forms
from .models import Inventory
from .validators import validate_isbn


# BookForm is a form based on the Book model for adding new books to the inventory
class InventoryForm(forms.ModelForm):
    isbn = forms.CharField(validators=[validate_isbn], max_length=17, help_text="Enter a valid ISBN-10 or ISBN-13.")

    class Meta:
        model = Inventory  # Links the form to the Book model
        fields = ['title', 'author', 'genre', 'publication_date', 'isbn']  # Specifies fields to include in the form
