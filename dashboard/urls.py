from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_asset, name='add_asset'),
    path('edit/<int:asset_id>/', views.edit_asset, name='edit_asset'),
    path('price-history/<int:asset_id>/', views.price_history, name='price_history'),
]