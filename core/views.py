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

@login_required(login_url='/login/')
def evento(request):
    return render(request,'evento.html')

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        título = request.POST.get('título')
        data_evento = request.POST.get('data_evento')
        descrição = request.POST.get('descrição')
        local = request.POST.get('local')
        usuário = request.user
        Evento.objects.create(título=título,
                              data_evento=data_evento,
                              local=local,
                              descrição=descrição,
                              usuário=usuário)
    return redirect('/')
