from django.db import models
from .validators import validate_isbn

# Define the inventory model which represents a single book entry in the database
class Inventory(models.Model):
    # Entry ID, as a primary key and auto-incremented
    entry_id = models.AutoField(primary_key=True)

    # The title of the book (string, max length 255)
    title = models.CharField(max_length=255)

    # The author of the book (string, max length 255)
    author = models.CharField(max_length=255)

    # Genre or category of the book (string, max length 100)
    genre = models.CharField(max_length=100)

    # The date the book was published (date field)
    publication_date = models.DateField(null=True)

    # The ISBN number of the book, unique identifier (string, max length 13)
    isbn = models.CharField(max_length=17, unique=True, validators=[validate_isbn])

    class Meta:
        db_table = 'Inventory'  # Specify the database table name

    # String representation of the Book object, useful for displaying book entries
    def __str__(self):
        return f"{self.title} by {self.author}"
