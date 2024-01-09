from django.urls import path
from .import views
from .views import AlunoCreateView, AlunoUpdateView


urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),
    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'),
    path('professorView', views.professorView, name='professor-lista'),
    path('professorID/<int:id>', views.professorIDview, name='professor-disciplina'),
    path('contato', views.contato_view, name='aluno-contato'),
    path('aluno/create', AlunoCreateView.as_view(), name='aluno-create'),
    path('aluno/<int:pk>/update/', AlunoUpdateView.as_view(), name='aluno-update'),
]
