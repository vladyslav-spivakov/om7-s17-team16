from django.shortcuts import redirect, render
from . import models

# Create your views here.


def index(request):
    return redirect('/book/')

def all_books(request):
    books = models.Book.get_all()
    
    context = {
        'is_empty' : not bool(books),
        'books' : books
    }

    return render(request, 'all_books.html', context)

def book_by_id(request, id_book):
    book = models.Book.get_by_id(id_book)
    context = {
        'not_found' : (book is None),
        'id' : id_book,
        'book' : book,
    }
    return render(request, 'book_by_id.html', context)