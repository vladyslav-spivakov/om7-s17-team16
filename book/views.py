from django.shortcuts import redirect, render
from . import models

# Create your views here.

def index(request):
    return redirect('/book/')

def all_books(request):
    books = models.Book.get_all()
    # books = [models.Book(id=102,name = "book1", description="Wow"), models.Book(id=103,name = "book2"), models.Book(id=104,name = "book3"), ]
    print(not bool(books))
    context = {
        'is_empty' : not bool(books),
        'books' : books
    }

    return render(request, 'all_books.html', context)