from django.urls import path
from . import views


urlpatterns = [
    path('', views.order_by_created_at),
    path('sort_by_end', views.order_by_plated_end_at),
    path('user_<int:user_id>', views.order_from_specific_user),
    path('over_dated', views.over_dated_orders)
    
]