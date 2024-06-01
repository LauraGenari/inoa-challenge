# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.asset_list, name='asset_list'),
    path('new/', views.asset_create, name='asset_create'),
    path('edit/<int:pk>/', views.asset_update, name='asset_update'),
    path('delete/<int:pk>/', views.asset_delete, name='asset_delete'),
    path('price-history/<int:pk>/', views.price_history, name='price_history'),
]
