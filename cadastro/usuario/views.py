from django.shortcuts import render, redirect
from .forms import NovoRegistroForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def cadastro(request):
    form = NovoRegistroForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        novo_usuario = User(username=username)
        novo_usuario.set_password(password)
        novo_usuario.save()
        login(request, novo_usuario)
        messages.success(request, "Registrado")

        return redirect("index")
    return render(request, "register.html", context)



def logar(request):
    form = LoginForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        usuario = form.cleaned_data.get("username")
        senha = form.cleaned_data.get("password")
        user = authenticate(username=usuario, password=senha)
        if user is None:
            messages.warning(request, "Acesso negado")
            return render(request, "login.html", context)
        messages.success(request, "Acesso permitido.")
        login(request, user)

        return redirect("index")
    return render(request, "login.html", context)


def sair(request):
    logout(request)
    return redirect("index")

def index(request):
    return render(request, "index.html")

