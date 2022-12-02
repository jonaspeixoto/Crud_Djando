from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClientForm
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

