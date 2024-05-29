from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import FormProduto

def home(request):
    produto = Produto.objects.all()

    dados = {
        'produtos' : produto
    }
  
    return render(request, 'home.html', dados)


def dashboard(request):
    produto = Produto.objects.all()

    dados = {
        'produtos' : produto
    }
  
    return render(request, 'dashboard.html', dados)


def addProduto(request):
    if request.method == 'POST':
        formProduto = FormProduto(request.POST, request.FILES)
        if formProduto.is_valid():
            formProduto.save()
            return redirect('dashboard')
    else:
        formProduto = FormProduto()
    
    context = {
        'form': formProduto
    }
    return render(request, 'addProduto.html', context)

def editarProduto(request, id_produto):
    produto = get_object_or_404(Produto, id=id_produto)
    
    if request.method == 'POST':
        formProduto = FormProduto(request.POST, request.FILES, instance=produto)
        if formProduto.is_valid():
            formProduto.save()
            return redirect('dashboard')
    else:
        formProduto = FormProduto(instance=produto)
    
    context = {
        'form': formProduto,
        'produto': produto
    }
    return render(request, 'editarProduto.html', context)

def excluirProduto(request, id_produto):
    produto = Produto.objects.get(id=id_produto)
    produto.delete()
    return redirect('dashboard')