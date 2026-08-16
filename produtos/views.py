from django.shortcuts import render

from .models import Produto


def produtos_home(request):
    produtos = Produto.objects.all().order_by('nome')

    contexto = {
        'nome': 'Gabriel Dev',
        'produtos': produtos,
    }


    return render(request, 'produtos/produtos.html', contexto)

