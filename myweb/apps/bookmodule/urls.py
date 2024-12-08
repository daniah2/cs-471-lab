from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('viewbook/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/text/formatting', views.format, name="books.format"),
    path('html5/listing', views.listing, name="books.listing"),
    path('html5/links', views.link, name= "books.link"),
    path('html5/tables', views.tables, name= "books.tables"),
    path('search/', views.search, name= "books.search"),
    path('createBook/', views.createBook, name= "books.createBook"),
    path('simple/query/', views.simple_query, name='books.simple_query'),
    path('lookup/query', views.lookup_query, name='books.lookup_query'),
    path('lab8/task1/', views.task1, name= "books.task1"),
    path('lab8/task2/', views.task2, name= "books.task2"),
    path('lab8/task3/', views.task3, name= "books.task3"),
    path('lab8/task4/', views.task4, name= "books.task4"),
    path('lab8/task5/', views.task5, name= "books.task5"),
    path('lab9_part1/listbooks/', views.list_books, name='books.listbooks'),
    path('lab9_part1/addbook/', views.add_book, name='books.addbook'),
    path('lab9_part1/editbook/<int:id>/', views.edit_book, name='books.editbook'),
    path('lab9_part1/deletebook/<int:id>/', views.delete_book, name='books.deletebook'),
    path('lab9_part2/listbooks/', views.list_books_with_forms, name='books.listbooks'),
    path('lab9_part2/addbook/', views.add_book_with_form, name='books.addbook'),
    path('lab9_part2/editbook/<int:id>/', views.edit_book_with_form, name='books.editbook'),
    path('lab9_part2/deletebook/<int:id>/', views.delete_book_with_form, name='books.deletebook'),



]
