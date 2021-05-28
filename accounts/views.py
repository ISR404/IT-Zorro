from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string

from .forms import UserLoginForm, UserRegisterForm


# Create your views here.

def login_view(request):
    title = "Войти"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('studentfood:profile')
    return render(request, "studentfood/html/registration/login.html", {"form": form, "title": title})


def register_view(request):
    title = "Зарегистрироваться"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("studentfood:profile")
    context = {
        "form": form,
        "title": title,
    }
    return render(request, "studentfood/html/registration/register.html", context)

def logout_view(request):
    logout(request)
    return redirect('studentfood:main')


def checkEmail(request):
    data = {}
    email = ''
    if request.method == "POST":
        email = request.POST.get('email')

        result = re.search(r'[\w\.-]+@[\w-]+\.[\w]{2,4}', email)

        if result:
            data = {
                'message': 'Email указан правильно!',
                'match': result.group(0)
            }
        else:
            data = {
                'message': 'Email указан некорректно!',
            }

    return JsonResponse(data)
