from django.urls import path
from .views import *

urlpatterns = [
    path('get-all-books/', GetAllBooks.as_view()),
    path('get-fav-books/', GetFavBooks.as_view()), 
    path('update-fav-book/<int:pk>/', UpdateFavBooks.as_view()), 
    path('create-book/', PostModelData.as_view()), 
    path('search/', SearchData.as_view()),  
    path('delete/<int:pk>/', DeleteData.as_view()), 
]
