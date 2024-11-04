# urls.py
from django.urls import path
from . import views

# Define URL patterns and map them to corresponding view functions
urlpatterns = [
    path(
        '',
        views.homepage,
        name='home'
    ),  # URL pattern for the homepage. An empty string corresponds to the root URL.

    path(
        'add-book/',
        views.add_book,
        name='add_book'
    ),  # URL pattern for adding a new book. The URL will be '/add-book/'.

    path(
        'view-books/',
        views.view_books,
        name='view_books'
    ),  # URL pattern for viewing all books in the inventory. The URL will be '/view-books/'.

    path(
        'export-books/<str:format>/',
        views.export_books,
        name='export_books'
    )  # URL pattern for exporting books data in specified format (e.g., JSON, CSV).
    # The format is passed as a URL parameter, allowing dynamic handling of export types.
]
