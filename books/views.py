from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookForm, BookUpdateForm
from .models import Books, Purchase
from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    query = request.GET.get('query', "") 
    genres = Books.objects.values_list('genre', flat=True).distinct() 
    
    if query:
        books = Books.objects.filter(Q(genre=query) | Q(title__icontains=query))
    else:
        books = Books.objects.all()
    
    paginator = Paginator(books, 3)
    page_number = request.GET.get('page')

    try:
        books = paginator.page(page_number)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    context = {"books": books, "headline": "Book", "genres": genres}
    return render(request, 'books/home.html', context)



def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES) 
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


def update_book(request, id):
    book = get_object_or_404(Books, id=id)
    book_form = BookUpdateForm(instance=book)

    if request.method == "POST":
        book_form = BookUpdateForm(request.POST, instance=book)

        if book_form.is_valid():
            book_form.save()
            return redirect('book_detail', id=id)  
        
    return render(request, 'books/update_book.html', {
        'book_form': book_form,
        'book': book
    })



@login_required
def buy_book(request, id):
    book = get_object_or_404(Books, id=id)
    
    if request.method == "POST":
        Purchase.objects.create(user=request.user, book=book)
        
        send_mail(
            subject="Successfully Purchased the Book.",
            message=f"You have successfully purchased the book. '{book.title}'.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email],
            fail_silently=False,
        )

        return redirect('home')

    return render(request, 'books/buy_book.html', {'book': book})