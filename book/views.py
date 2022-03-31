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