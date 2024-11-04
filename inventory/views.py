from django.shortcuts import render, redirect
from .models import Inventory
from .forms import InventoryForm
import pandas as pd
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, ValidationError


# Homepage view: displays the main navigation options
def homepage(request):
    """Renders the homepage for the Book Inventory Management system."""
    return render(request, 'inventory/homepage.html')


# View for adding a new book to the inventory
def add_book(request):
    """Handles adding a new book entry to the inventory.

    If the request is a POST, it processes the form data. If the form is valid,
    it saves the new book to the database and redirects to the view_books page.
    If the form is invalid, it displays errors.

    Returns:
        HttpResponse: Rendered add book page with form context or redirects to view_books.
    """
    if request.method == 'POST':
        form = InventoryForm(request.POST)

        if form.is_valid():
            try:
                form.save()  # Save the new book to the database
                messages.success(request, 'Book added successfully.')  # Success message
                return redirect('view_books')  # Redirect to the view_books page
            except Exception as e:
                messages.error(request, f'An error occurred while adding the book: {str(e)}')  # Error handling
        else:
            messages.error(request, 'Please correct the errors below.')  # Form validation error
    else:
        form = InventoryForm()  # Create a blank form for GET requests

    return render(request, 'inventory/add_book.html', {'form': form})  # Render the add book form


# View for displaying all books in the inventory with filtering capabilities
def view_books(request):
    """
    Fetches and displays all books in the inventory with options to filter by title,
    author, genre, and publication date.

    Returns:
        HttpResponse: Rendered view_books page with filtered books and query context.
    """
    title_query = request.GET.get('title', '')
    author_query = request.GET.get('author', '')
    genre_query = request.GET.get('genre', '')
    publication_date_query = request.GET.get('publication_date', '')

    # Start with all books and filter based on the provided criteria
    try:
        books = Inventory.objects.all()  # Fetch all books
        if title_query:
            books = books.filter(title__icontains=title_query)
        if author_query:
            books = books.filter(author__icontains=author_query)
        if genre_query:
            books = books.filter(genre__icontains=genre_query)
        if publication_date_query:
            books = books.filter(publication_date__icontains=publication_date_query)

    except Exception as e:
        messages.error(request, f'An error occurred while retrieving books: {str(e)}')  # Handle unexpected errors
        books = []  # Set books to an empty list if an error occurs

    context = {
        'books': books,
        'title_query': title_query,
        'author_query': author_query,
        'genre_query': genre_query,
        'publication_date_query': publication_date_query,
    }

    return render(request, 'inventory/view_books.html', context)  # Render the view_books page


# View for exporting books as a CSV file or JSON
def export_books(request, format: str) -> HttpResponse:
    """
    Exports book inventory data in either JSON or CSV format.

    Args:
        format (str): The format for exporting the data, either 'json' or 'csv'.

    Returns:
        HttpResponse: JSON response or CSV file response.
    """
    try:
        books = Inventory.objects.all()
        data = list(books.values())  # Convert QuerySet to list of dictionaries

        if format == 'json':
            return JsonResponse(data, safe=False)  # Return JSON response

        elif format == 'csv':
            df = pd.DataFrame(data)  # Create DataFrame from data
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="books.csv"'  # Set the filename
            df.to_csv(path_or_buf=response, index=False)  # Write DataFrame to response
            return response  # Return CSV response

        else:
            messages.error(request, 'Invalid export format requested.')  # Handle invalid format
            return redirect('view_books')  # Redirect if the format is invalid

    except ObjectDoesNotExist:
        messages.error(request, 'No books found for export.')  # Handle no books found
        return redirect('view_books')  # Redirect if no books exist

    except Exception as e:
        messages.error(request, f'An error occurred while exporting books: {str(e)}')  # Handle unexpected errors
        return redirect('view_books')  # Redirect on error
