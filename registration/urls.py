from django.urls import path
from . import views

#same as route files on nodeJS
urlpatterns = [
    path('stocks/', views.get_stocks)
]