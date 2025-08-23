from django.shortcuts import render
from django.http import HttpResponse


def pagina_inicial(request):
    return render(request, 'home.html', {'nome': 'Tiago'})


def dashboards(request):
    return HttpResponse('Estatísticas do Site')
