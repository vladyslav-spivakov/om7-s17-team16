from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book/', views.all_books),
    # path('book/<int:id_book>/', views.book_edit),
    
]
