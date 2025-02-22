from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookForm
from .models import Books
from django.contrib.auth.decorators import login_required 
from django.db.models import Q

def home(request):
    query = request.GET.get('query', "") 
    genres = Books.objects.values_list('genre', flat=True).distinct() 
    
    if query:
        books = Books.objects.filter(genre=query) or Books.objects.filter(title__icontains = query)

    else:
        books = Books.objects.filter()

    context = {"books": books, "headline": "Book", "genres": genres}
    return render(request, 'books/home.html', context)



def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()

    return render(request, 'books/add_book.html', {'form': form})


def book_details(request, id):

    book = get_object_or_404(Books, id=id)
    

    return render(request, 'books/book_detail.html', { 'book': book })


@login_required(login_url='/login/')

def delete_book(request, id):
    book = Books.objects.get(id=id)

    if request.method == 'POST':
        book.delete()

        return redirect('home')
    return render(request, "books/delete_book.html", {'book' : book})