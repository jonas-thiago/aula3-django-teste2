from django.shortcuts import render
from django.http import HttpResponse
from .models import Aluno, Professor

# Create your views here.

def alunoView(request):
    alunos_list =Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list': alunos_list})

def professorView(request):
    professor_list = Professor.objects.all()
    return render(request, 'main/professor.html', {'professor_list': professor_list})

def contato_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print('name', name)
        print('Email', email)
        print('Message', message)

    return render(request, 'main/contato.html')
