from django.urls import path
from . import views


urlpatterns = [
    path('', views.order_by_created_at),
    path('sort_by_end', views.order_by_plated_end_at),
    
]