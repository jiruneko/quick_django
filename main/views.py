from multiprocessing import context
from .models import Book
from django.shortcuts import render
from django.http import HttpResponse

def list(request):
  books = Book.objects.all()
  return render(request, 'main/list.html',{
    'books': books
  })
