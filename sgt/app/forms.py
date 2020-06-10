from django import forms
from .models import Curso, Disciplina, Docente

class DisciplinaForm(forms.ModelForm):
	# curso = forms.ModelChoiceField(queryset=Curso.objects.all())

	class Meta:
		model = Disciplina
		fields = '__all__'


class DocenteForm(forms.ModelForm):
	# curso = forms.ModelChoiceField(queryset=Curso.objects.all())
	senha = forms.CharField(max_length=32, widget=forms.PasswordInput) 

	class Meta:
		model = Docente
		fields = ('nome', 'curso', 'email', 'siape',)