from django.shortcuts import render, redirect
from django.template.context_processors import request

from .models import Cliente
from .forms import ClientForm
from django.http import HttpResponse
from .entidades import cliente
from .service import cliente_service
# Create your views here.


def listar_clientes(request):
    clientes = cliente_service.listar_clientes()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def inserir_cliente(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            sexo = form.cleaned_data["sexo"]
            print(sexo)
            data_nascimento = form.cleaned_data["data_nascimento"]
            email = form.cleaned_data["email"]
            profissao = form.cleaned_data["profissao"]
            cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento,
                                           email=email, profissao=profissao)
            print(cliente_novo.data_nascimento)
            cliente_service.cadastrar_cliente(cliente_novo)
            return redirect('listar_clientes')
    else:
        form = ClientForm()
    return render(request, 'clientes/form_clientes.html', {'form': form})


def listar_cliente_id(request, id):
    clientes = cliente_service.listar_cliente_id(id)
    return render(request, 'clientes/lista_cliente.html', {'cliente': clientes})


def editar_cliente(request, id):
    clientes = cliente_service.listar_cliente_id(id)
    form = ClientForm(request.POST or None, instance=clientes)
    if form.is_valid():
        nome = form.cleaned_data["nome"]
        sexo = form.cleaned_data["sexo"]
        data_nascimento = form.cleaned_data["data_nascimento"]
        email = form.cleaned_data["email"]
        profissao = form.cleaned_data["profissao"]
        cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, data_nascimento=data_nascimento,
                                       email=email, profissao=profissao)
        cliente_service.editar_cliente(clientes, cliente_novo)
        return redirect('listar_clientes')
    return render(request, 'clientes/form_clientes.html', {'form': form})


def remover_cliente(request, id):
    clientes = cliente_service.listar_cliente_id(id)
    if request.method == "POST":
        cliente_service.remover_cliente(clientes)
        return redirect('listar_clientes')
    return render(request, 'clientes/confirma_exclusao.html', {'cliente': clientes})
