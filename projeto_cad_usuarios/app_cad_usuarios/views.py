from django.shortcuts import render
from .models import usuario
from django.http import HttpResponseBadRequest

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        # Criando um novo usuário
        novo_usuario = usuario()

        # Capturando os dados do formulário
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        # Verificando se o campo 'idade' é numérico
        if not idade.isdigit():  # Verifica se o valor de 'idade' contém apenas dígitos
            return HttpResponseBadRequest("O campo 'idade' precisa ser um número.")

        # Salvando os dados no banco
        novo_usuario.nome = nome
        novo_usuario.idade = int(idade)  # Convertendo a idade para inteiro antes de salvar
        novo_usuario.save()

        # Exibindo todos os usuários cadastrados
        context = {
            'usuarios': usuario.objects.all()
        }

        # Retornando para a página 'usuarios.html'
        return render(request, 'usuarios/usuarios.html', context)
    
    return render(request, 'usuarios/usuarios.html')
