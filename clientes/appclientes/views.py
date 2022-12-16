from django.shortcuts import render, redirect
from django.template.context_processors import request

from .models import Cliente
from .forms import ClientForm
from django.http import HttpResponse
# Create your views here.


def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})


def inserir_cliente(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_clientes')
    else:
        form = ClientForm()
    return render(request, 'clientes/form_clientes.html', {'form': form})


def listar_cliente_id(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, 'clientes/lista_cliente.html', {'cliente': cliente})


def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClientForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/form_clientes.html', {'form': form})
