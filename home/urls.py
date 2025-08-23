from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.pagina_inicial, name='pagina_inicial'),
    path('dashboard/', views.dashboards, name='estatisticas'),
]
