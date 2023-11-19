from django.shortcuts import render
from .models import Book

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

class BookListView(ListView):
    model = Book

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    success_url ='/'

class BookDetailView(DetailView):
    model = Book

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    success_url ='/'


    
