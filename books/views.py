from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required

from books.models import Book, Category
from .forms import EditBookForm, NewBookForm

from django.db.models import Q

# Create your views here.
@login_required
def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Book.objects.all()
    
    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query)|Q(description__icontains=query))

    return render(request, 'books/items.html', {'items': items, 'query':query, 'categories': categories, 'category_id': int(category_id)})

@login_required
def detail(request, pk):
    item = get_object_or_404(Book, pk=pk)
    related_items = Book.objects.filter(category=item.category).exclude(pk=pk)[:3]


    return render(request, 'books/detail.html', {'item': item, 'related_items': related_items})
    

@login_required
def new(request):
    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('books:detail', pk=item.id)
    else:
        form = NewBookForm()

    return render(request, 'books/form.html', {'form': form, 'title': 'New Item'})



@login_required
def edit(request, pk):
    item = get_object_or_404(Book, pk=pk, created_by=request.user)


    if request.method == 'POST':
        form = EditBookForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('books:edit', pk=item.id)
    else:
        form = EditBookForm(instance=item)

    return render(request, 'books/edit.html', {'form': form, 'title': 'Edit Item'})



@login_required
def delete(request, pk):
    item = get_object_or_404(Book, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')