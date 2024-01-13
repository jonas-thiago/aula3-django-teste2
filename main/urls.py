from django.urls import path
from .import views
from .views import AlunoCreateView, AlunoUpdateView, ProfessorCreateView, ProfessorUpdateView


urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),
    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'),
    path('professor', views.professorView, name='professor-lista'),
    path('professorID/<int:id>', views.professorIDview, name='professor-disciplina'),
    path('contato', views.contato_view, name='aluno-contato'),
    path('aluno/create', AlunoCreateView.as_view(), name='aluno-create'),
    path('aluno/<int:pk>/update/', AlunoUpdateView.as_view(), name='aluno-update'),
    path('professor/create', ProfessorCreateView.as_view(), name='professor-create'),
    path('professor/<int:pk>/update/', ProfessorUpdateView.as_view(), name='professor-update'),
    
]
