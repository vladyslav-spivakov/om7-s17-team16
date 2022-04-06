from django.urls import path
from . import views

urlpatterns = [
    path('', views.authors_update),
    path('<int:id>', views.authors_update),
    path('list', views.author_list),
    
]
