
from django.shortcuts import render, get_object_or_404


from django.contrib.auth.decorators import login_required

from books.models import Book

# Create your views here.

@login_required
def index(request):
    items = Book.objects.all()

    return render(request, 'dashboard/index.html', {'items': items})