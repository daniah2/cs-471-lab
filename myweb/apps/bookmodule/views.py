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

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]
    
def search(request):
    newBooks = []
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): 
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained: 
                newBooks.append(item)
    return render(request, "bookmodule/bookList.html",{'books':newBooks})