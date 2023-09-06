from django.shortcuts import redirect, render


from books.models import Category, Book

from .forms import SignupForm

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    items = Book.objects.all()[:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {'categories': categories, 'items': items,})


def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/login/')