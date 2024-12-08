from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import *
from django.db.models import Q , Count, Sum, Avg, Max, Min

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

def createBook(request):
   if request.method == "POST":
      title = request.POST.get('title')
      author = request.POST.get('author')
      price = float(request.POST.get('price'))
      edition = int(request.POST.get('edition'))
 
      #usingg constructor
      mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', price = 100.0, edition = 1)
      #using create 
      mybooks = Book.objects.create(title = 'Continuous Delivery', author = 'J.Humble and D. Farley',price = 10.0, edition = 1)
      mybook.save() 
      mybooks.save()
      #from user
      myb = Book(title = title, author=author, price=price,edition = edition)
      myb.save()
      books = Book.objects.all()

      #return redirect('bookmodule:bookList')
      return render(request,'bookmodule/booksListDemo.html',{'books': books})
   return  render(request,'bookmodule/createBook.html')

def simple_query(request):
   #Single object
   #mybook = Book.objects.get(title = 'Continuous Delivery')
   #print(f"author of {mybook.title} is {mybook.author}")

   #multiple objects
   #mybooks = Book.objects.filter(title__icontains='and')
   #for obj in mybooks:
   #    print(f"author of {obj.title} is {obj.author}")
      
   #or for multiple objects
   myBooks = Book.objects.filter(title__icontains='and') 
   print(myBooks)
   return render(request, 'bookmodule/booksListDemo.html', {'books':myBooks})

def lookup_query(request):
   mybooks = books = Book.objects.filter(author__isnull =False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
   if len(mybooks) >= 1:
     return render(request,'bookmodule/bookList.html', {'books':mybooks})
   else:
     return render(request, 'bookmodule/index.html')
      
  
def insert_books():
    Book.objects.create(title="Continuous Delivery", author="J. Humble and D. Farley", price=120.00, edition=3)
    Book.objects.create(title="Reversing: Secrets of Reverse Engineering", author="E. Eilam", price=97.00, edition=2)
    Book.objects.create(title="The Hundred-Page Machine Learning Book", author="Andriy Burkov", price=100.00, edition=4)
    Book.objects.create(title="Clean Code", author="Robert C. Martin", price=55.00, edition=2)
    Book.objects.create(title="Design Patterns: Elements of Reusable Object-Oriented Software", author="Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides", price=75.00, edition=1)
    Book.objects.create(title="The Pragmatic Programmer", author="Andrew Hunt and David Thomas", price=50.00, edition=2)
    Book.objects.create(title="The Mythical Man-Month", author="Fred Brooks", price=60.00, edition=1)
    Book.objects.create(title="Introduction to Algorithms", author="Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein", price=150.00, edition=3)
    Book.objects.create(title="Refactoring: Improving the Design of Existing Code", author="Martin Fowler", price=45.00, edition=2)
    Book.objects.create(title="The Clean Coder: A Code of Conduct for Professional Programmers", author="Robert C. Martin", price=40.00, edition=1)


def task1(request):
    books = Book.objects.filter(Q(price__lte=50))
    return render(request,'bookmodule/task1.html',{'books':books})

def task2(request):
    books = Book.objects.filter(Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3(request):
    books = Book.objects.exclude(
        Q(edition__gt=2) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task4(request):
    books = Book.objects.order_by('title')
    return render(request, 'bookmodule/task2.html', {'books': books})

def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})
