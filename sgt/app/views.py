from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso, Disciplina, Docente
from .forms import DisciplinaForm, DocenteForm
from django.contrib.auth.models import User, Group


# Create your views here.
@login_required
def index(request):
	return render(request, 'app/index.html')

@login_required
def cursos_list(request):
	cursos = Curso.objects.all()
	context = {
		'cursos': cursos
	}
	return render(request, 'app/cursos_list.html', context)

@login_required
def disciplinas_list(request):
	disciplinas = Disciplina.objects.select_related('curso').all()

	context = {
		'disciplinas': disciplinas
	}
	return render(request, 'app/disciplinas_list.html', context)

@login_required
def disciplina_new(request):
	if (request.method == 'POST'):
		form = DisciplinaForm(request.POST)
		if (form.is_valid()):
			d = form.save()
			return redirect('disciplinas_list')
	else:
		form = DisciplinaForm()
	return render(request, 'app/disciplina_new.html', {'form':form})

@login_required
def disciplina_edit(request, pk):
	disciplina = get_object_or_404(Disciplina, pk=pk)	
	if (request.method == 'POST'):
		form = DisciplinaForm(request.POST, instance=disciplina)
		if (form.is_valid()):
			disciplina = form.save()
			return redirect('disciplinas_list')
	else:
		form = DisciplinaForm(instance=disciplina)
	return render(request, 'app/disciplina_new.html', {'form': form})

@login_required
def docentes_list(request):
	docentes = Docente.objects.select_related('curso').all()

	context = {
		'docentes': docentes
	}
	return render(request, 'app/docentes_list.html', context)


@login_required
def docente_new(request):
	if (request.method == 'POST'):
		form = DocenteForm(request.POST)
		if (form.is_valid()):
			email_sgt = form.cleaned_data["email"]
			usuario_sgt = email_sgt.split('@')[0]
			senha_sgt = form.cleaned_data["senha"]
			#criar usuario
			user = User.objects.create_user(usuario_sgt, email_sgt, senha_sgt)
			#add usuario ao grupo
			group = Group.objects.get(name='Tutor')
			user.groups.add(group)
			#salvar docente
			form.save()
			return redirect('docentes_list')
	else:
		form = DocenteForm()
	return render(request, 'app/docente_new.html', {'form':form})

@login_required
def docente_edit(request, pk):
	docente = get_object_or_404(Docente, pk=pk)	
	if (request.method == 'POST'):
		form = DocenteForm(request.POST, instance=docente)
		if (form.is_valid()):
			docente = form.save()
			return redirect('docentes_list')
	else:
		form = DocenteForm(instance=docente)
	return render(request, 'app/docente_new.html', {'form': form})


# 1. ADD SENHA NO FORM (A SENHA SERVIRÁ PARA A CRIAÇÃO DO USUÁRIO)
# 2. AO INSERIR DOCENTE, CRIAR USUÁRIO BASEADO NO E-MAIL
# 3. INSERIR NO GRUPO DE TUTORES

# from django.contrib.auth.models import User

# # Create user and save to the database
# user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

# # Update fields and then save again
# user.first_name = 'John'
# user.last_name = 'Citizen'
# user.save()

# ADICIONAR NO GRUPO DE TUTORES
# from django.contrib.auth.models import Group
# group = Group.objects.get(name='groupname')
# user.groups.add(group)

