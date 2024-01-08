from django.urls import path
from .import views


urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),
    path('professorView', views.professorView, name='professor-lista'),
]
