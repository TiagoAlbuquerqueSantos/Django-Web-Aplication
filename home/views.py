from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario


def pagina_inicial(request):
    if request.method == 'GET':
        return render(request, 'home.html', {'nome': 'Tiago'})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        user = Usuario.objects.filter(nome=nome)

      #  user = Usuario(nome=nome, idade=idade)
      #  user.save()

        return HttpResponse(f'O usuário {nome} foi cadastrado com sucesso!')


def dashboards(request):

    pessoas = Usuario.objects.all()
    return HttpResponse(pessoas)
