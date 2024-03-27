from django.shortcuts import render
from .models import produto
from .models import Usuario

# Create your views here.

def inicio(request):
    rel_produto = produto.objects.all()
    return render(request, 'usuarios/produtos.html', {'rel_produto': rel_produto})

def usuarios(request):
    #salvar dados para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    #exibir os usuarios
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados para a página de listagem
    return render(request, 'usuarios/usuarios.html', usuarios)