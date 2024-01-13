from django.shortcuts import render, redirect, get_object_or_404              # Atenção na importação
from django.http import HttpResponse
from .models import Aluno, Professor
from .forms import AlunoForm, ProfessorForm
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

# Create your views here.

def alunoView(request):
    alunos_list =Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list':alunos_list})

def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    return render(request, 'main/alunoID.html', {'aluno':aluno})

def professorView(request):
    professor_list = Professor.objects.all()
    return render(request, 'main/professor.html', {'professor_list':professor_list})

def professorIDview(request, id):
    professor = get_object_or_404(Professor, pk=id)
    return render(request, 'main/professorID.html', {'professor':professor})

def contato_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print('name', name)
        print('Email', email)
        print('Message', message)

    return render(request, 'main/contato.html')

'''def delete_aluno(request):
    aluno_delete = Aluno.objects.filter(id=id)
    return render(request, 'main/alunos.html', {'alunos_list':alunos_list})'''


class AlunoCreateView(CreateView):
    model = Aluno
    form_class = AlunoForm
    success_url = reverse_lazy('aluno-lista')       # url para redirecionar após a criação do objeto
    template_name = 'main/aluno_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
# outra forma seria por função em vez de classe

def aluno_create_view(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.user = request.user
            aluno.save()
            return redirect(reverse('aluno-lista'))
    else:
        form = AlunoForm()

    return render(request, 'aluno_form.html', {'form':form})


class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'main/aluno_form.html'
    success_url = reverse_lazy('aluno-lista')

class ProfessorCreateView(CreateView):
    model = Professor
    form_class = ProfessorForm
    success_url = reverse_lazy('professor-lista')       # url para redirecionar após a criação do objeto
    template_name = 'main/professor_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ProfessorUpdateView(UpdateView):
    model = Professor
    form_class = ProfessorForm
    template_name = 'main/professor_form.html'
    success_url = reverse_lazy('professor-lista')
