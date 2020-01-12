from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View, ListView
from .form import *
from .models import *
from .registration import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'main.html', locals())


def db(request):
    return render(request, 'db.html', locals())


def book_id(request, id):
    book = Book.objects.filter(id_book=id)
    book = book.first()
    review_filter = Issuance.objects.filter(book_name_id=id)
    review = list(review_filter)
    id = request.GET.get('id')
    if id:
        queryset = Book.objects.filter(id=id)
    return render(request, 'book_id.html', locals())


class ReaderView(ListView):
    model = User
    template_name = 'reader.html'


def books(request):
    form = BookForm(request.POST, request.FILES or None)
    if request.POST and form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('book_id_url', args=(instance.pk,)))
    return render(request, 'books.html', locals())


def registration(request):
    errors = {'username': '', 'password': '', 'password2': '', 'email': '', 'firstname': '', 'surname': ''}
    error_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
            error_flag = True
        elif len(username) < 5:
            errors['username'] = 'Логин должен превышать 5 символов'
            error_flag = True
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'
            error_flag = True
        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
            error_flag = True
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'
            error_flag = True
        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'
        if not error_flag:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname,
                                            last_name=surname)
            return HttpResponseRedirect('/login/')
    return render(request, 'registration.html', locals())


def login(request):
    error = ""
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/success/')
        else:
            error = "Попробуй ещё раз"
    return render(request, 'login.html', locals())


@login_required()
def success(request):
    return render(request, 'success.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/main/')


def registration2(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            first_name=request.POST.get('firstname'),
                                            last_name=request.POST.get('surname'))
            return HttpResponseRedirect('/login/')
    return render(request, 'registration2.html', {'form': form})


def ListBookView(request):
    book_model = Book.objects.all()
    book_list = list(book_model)
    # template_name = 'list_books.html'
    form = BookForm(request.POST, request.FILES or None)
    if request.POST and form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('book_id_url', args=(instance.pk,)))
    return render(request, 'list_books.html', locals())

def review_add(request):
    form = ReviewForm(request.POST, request.FILES or None)
    if request.POST and form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(reverse('book_id_url', args=(instance.pk,)))
    return render(request, 'books.html', locals())