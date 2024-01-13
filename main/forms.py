from django import forms 
from .models import Aluno, Professor

class AlunoForm(forms.ModelForm):
    # Mascara do telefone(funciona com JS.)
    telefone = forms.CharField(widget=forms.TextInput(attrs={'minlength':'15', 'maxlength':'15','onkeyup':'handlePhone(event)'}))
    # Calendário no input
    data_nascimento = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))

    class Meta:
        model = Aluno
        fields = ['nome','telefone','email','data_nascimento','descricao']

    def _init_(self, *args, **kwargs):
        super()._init_(args,*kwargs)
        self.fields['nome'].widget.attrs.update({'class':'form-control'})
        self.fields['telefone'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['data_nascimento'].widget.attrs.update({'class':'form-control'})
        self.fields['descricao'].widget.attrs.update({'class':'form-control'})
        #self.fields['status'].widget.attrs.update({'class':'form-control'})


class ProfessorForm(forms.ModelForm):
    # Mascara do telefone(funciona com JS.)
    telefone = forms.CharField(widget=forms.TextInput(attrs={'minlength':'15', 'maxlength':'15','onkeyup':'handlePhone(event)'}))
    # Calendário no input
    data_nascimento = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))

    class Meta:
        model = Professor
        fields = ['nome_professor','telefone_professor','email_professor','disciplina']

    def _init_(self, *args, **kwargs):
        super()._init_(args,*kwargs)
        self.fields['nome_professor'].widget.attrs.update({'class':'form-control'})
        self.fields['telefone_professor'].widget.attrs.update({'class':'form-control'})
        self.fields['email_professor'].widget.attrs.update({'class':'form-control'})
        self.fields['disciplina'].widget.attrs.update({'class':'form-control'})
        #self.fields['status'].widget.attrs.update({'class':'form-control'})