from django.shortcuts import render, HttpResponse, redirect
from .models import books


# Create your views here.
def table(request):
    data = books.objects.all()
    return render(request, 'page.html', {'data': data})


def form(request):
    if request.method == "POST":
        book_obj = books()
        book_obj.bookid=request.POST.get('bookid')
        book_obj.name = request.POST.get('name')
        book_obj.author = request.POST.get('author')
        book_obj.description = request.POST.get('description')
        book_obj.image = request.POST.get('image')
        book_obj.save()
        return redirect('/page')
    return render(request, 'form.html')


def info(request, id):
    data = books.objects.get(bookid=id)
    return render(request, 'info.html', {'data': data})


def delete(request, id):
    data = books.objects.get(bookid=id)
    data.delete()
    return redirect('/page')


def update(request, id):
    data1 = books.objects.get(bookid=id)
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        author = data.get('author')
        description = data.get('description')

        data1.name = name
        data1.author = author
        data1.description = description
        data1.save()
        return redirect('/page')
    return render(request, 'update.html', {'data': data1})
