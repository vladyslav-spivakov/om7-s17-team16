from django.shortcuts import render
from . import models
from authentication.models import CustomUser
from book.models import Book
import datetime
# Create your views here.

def order_by_created_at(request):

    orders = list(models.Order.objects.all().order_by("created_at"))
    
    content = {
        'is_empty': bool(orders),
        "orders": orders,
        'sorted_by': 'the data of creation',
    }
    return render(request, "order_sorted.html", content)


def order_by_plated_end_at(request):

    orders = list(models.Order.objects.all().order_by("plated_end_at"))
    
    content = {
        'is_empty': bool(orders),
        "orders": orders,
        'sorted_by': 'the data of an order\'s ending',
    }
    return render(request, "order_sorted.html", content)