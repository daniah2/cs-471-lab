from django.http import HttpResponse
from django.shortcuts import render

def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')
def link(request):
    return render(request, 'bookmodule/links.html')
def format(request):
    return render(request, 'bookmodule/fomat.html')
def listing(request):
    return render(request, 'bookmodule/lists.html')
def tables(request):
    return render(request, 'bookmodule/tables.html')