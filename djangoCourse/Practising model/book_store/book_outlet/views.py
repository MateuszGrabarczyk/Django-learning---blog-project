from django.shortcuts import get_object_or_404, render
from .models import Book
# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", {
        "books": books
    })

def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    return render(request, "book_outlet/book_detail.html", {
        "book": book
    })