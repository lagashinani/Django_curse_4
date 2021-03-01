from django.shortcuts import render
from .models import Book


def books_view(request, date=None):
    next_page = None
    prev_page = None
    template = 'books/books_list.html'
    if date:
        books = Book.objects.filter(pub_date=date)
        next_books = Book.objects.filter(pub_date__gt=date).order_by('pub_date')
        prev_books = Book.objects.filter(pub_date__lt=date).order_by('-pub_date')
        if len(next_books):
            next_page = next_books[0]
        if len(prev_books):
            prev_page = prev_books[0]
    else:
        books = Book.objects.all()
    context = {'books': books, 'next_page': next_page, 'prev_page': prev_page}
    return render(request, template, context)
