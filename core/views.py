from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# def index(request):
#     return redirect('/agenda/')
def login_user(request):
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuráio = authenticate(username=username, password=password)
        if usuráio is not None:
            login(request, usuráio)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválidos!")

    return redirect('/')
@login_required(login_url='/login/')
def lista_eventos(request):
    usuário = request.user
    evento = Evento.objects.filter(usuário=usuário)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)