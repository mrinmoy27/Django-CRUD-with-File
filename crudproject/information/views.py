import os
from django.shortcuts import render, redirect
from . forms import UserForm
from . models import User
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'information/index.html')


def user_list(request):
    users = User.objects.all()

    paginator = Paginator(users, 2)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'information/list.html', {'users': page_object})


def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/success/')
    else:
        form = UserForm()
    return render(request, 'information/add.html', {'form': form})

def add_success(request):
    return render(request, 'information/success.html')

def edit(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserForm(request.POST or None, request.FILES or None, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/list/')
    else:
        form = UserForm(instance=user)
    return render(request, 'information/edit.html', {'form': form})


def delete(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        if len(user.photo) > 0:
            os.remove(user.photo.path)
        user.delete()
        return redirect('/list/')
    return render(request, 'information/delete.html')

def view(request, id):
    user = User.objects.get(id=id)
    return render(request, 'information/view.html', {'user': user})
