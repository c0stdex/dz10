from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('quotes/', views.quote_list, name='quote_list'),
    path('search/', views.search, name='search'),
    path('top_ten_tags/', views.top_ten_tags, name='top_ten_tags'),
]
