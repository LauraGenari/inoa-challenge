from django.urls import path
from . import views

#same as route files on nodeJS
urlpatterns = [
    path('', views.set_stocks_to_email),
]