from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_list, name='orders_list'),
    path('add/', views.add_order, name='add_order'),
    path('delete/<int:order_id>/', views.delete_order, name='delete_order'),
    path('update/<int:order_id>/', views.update_status, name='update_status'),
    path('edit/<int:order_id>/', views.edit_order, name='edit_order'),
    path('revenue/', views.calculate_revenue, name='calculate_revenue'),
    path('api/orders/', views.api_orders_list, name='api_orders_list'),
]