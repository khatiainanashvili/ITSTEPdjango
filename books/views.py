from django.shortcuts import redirect, render
from .forms import BookForm
from .models import Books

def home(request):
    books = Books.objects.all()
    headline = "Book"
    context = {"books": books, "headline": headline}
    return render(request, 'books/book_list.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'books/add_book.html', {'form': form})