from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def produtos_home(request):
    contexto = {
        "nome": "Gabriel Dev",
    }

    return render(request, 'produtos/produtos.html', contexto)

