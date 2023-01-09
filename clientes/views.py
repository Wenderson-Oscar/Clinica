from django.shortcuts import render, redirect, get_object_or_404
from clientes.forms import ClientesForm, UserCreateForm
from django.contrib.auth import authenticate, login, logout
from clientes.models import Clientes
from medico.models import Agenda
from django.contrib.auth.models import User


def home(request):
    return render(request, 'usuarios/home.html')

def listar_agendas(request):
    agendas = Agenda.objects.all()
    return render(request, 'usuarios/listar_agenda.html', {'agendas':agendas})

def detalhar_agenda(request, id):
    agenda = get_object_or_404(Agenda, pk=id)
    return render(request, 'usuarios/detalhar_agenda.html', {'agenda':agenda})

def marcar_consulta(request, id, pk):
    agenda = get_object_or_404(Agenda, pk=id)
    cliente = get_object_or_404(Clientes, pk=pk)
    cliente.consulta.add(agenda)
    return render(request, 'usuarios/area_cliente.html', {'cliente': cliente})

def area_do_cliente(request,id):
    cliente = get_object_or_404(Clientes, id=id)
    return render(request, 'usuarios/area_cliente.html',{'cliente':cliente})

# Cadastro / Autenticação / Login #

def login_adm(request):
    return render(request, 'usuarios/login_adm.html', {})

def administracao(request, id):
    adm = get_object_or_404(User, id=id)
    return render(request, 'usuarios/administracao.html',{'adm': adm})

def autenticar_administrador(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_superuser:
        login(request, user)
        id = user.id
        adm = get_object_or_404(User, pk=id)
        return render(request, 'usuarios/administracao.html',{'adm':adm})
    elif user is not None:
        return autenticar_usuario(request)
    else:
        return render(request, 'usuarios/home.html',{})

def create_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('cadastro_cliente')
    else:
        form = UserCreateForm()
    return render(request, 'usuarios/cadastrar_cliente.html',{'form': form})

def cadastrar_cliente(request):
    if request.method == "POST":
        form = ClientesForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user=request.user
            cliente.save()
            form.save()
            return redirect('area_cliente', id=cliente.id)
    else:                                                                                                                                                                                                                                                                                     
        form = ClientesForm()
    return render(request, 'usuarios/cadastrar_cliente.html', {'form':form})

def autenticar_usuario(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        id = user.id
        cliente = get_object_or_404(Clientes, pk=id)
        return render(request, 'usuarios/area_cliente.html', {'cliente': cliente})
    else:
        return render(request, 'usuarios/home.html')
 
def logout_usuario(request):
    logout(request)
    return render(request, 'usuarios/home.html',{})

def page_login(request):
    return render(request, 'usuarios/page_login.html',{})