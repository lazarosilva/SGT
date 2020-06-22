from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso, Disciplina, Docente, Discente
from .forms import DisciplinaForm, DocenteForm, DiscenteForm
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

@login_required
def discentes_list(request):
	discentes = Discente.objects.select_related('curso').all()

	context = {
		'discentes': discentes
	}
	return render(request, 'app/discentes_list.html', context)

@login_required
def discente_new(request):

	if (request.method == 'POST'):
		mthd = 'p'
		form = DiscenteForm(request.POST, mthd=mthd, tt='add', om='', op='', fct='add', fog='add', ppe='add', ppp='add')
		if (form.is_valid()):
			discente = form.save(commit=False)
			if (form.cleaned_data["motivo_escolha_curso"] == 'O'):
				discente.motivo_escolha_curso = form.cleaned_data["outro_motivo"]

			if (form.cleaned_data["plano_egresso"] == 'O'):
				discente.plano_egresso = form.cleaned_data["outro_plano"]
			
			discente.save()
			return redirect('discentes_list')
	else:
		mthd = 'g'
		form = DiscenteForm(mthd=mthd, tt='add', om='', op='', fct='add', fog='add', ppe='add', ppp='add')

	return render(request, 'app/discente_new.html', {'form':form})

@login_required
def discente_edit(request, pk):
	discente = get_object_or_404(Discente, pk=pk)
	mthd = ''
	tt = ''
	om = ''
	op = ''
	fct = 'add'
	fog = 'add'
	ppe = 'add'
	ppp = 'add'

	if (request.method == 'POST'):
		mthd = 'p'
		form = DiscenteForm(request.POST, instance=discente, mthd=mthd, tt=tt, om=om, op=op, fct=fct, fog=fog, ppe=ppe, ppp=ppp)
		if(form.is_valid()):	
			if (form.cleaned_data["motivo_escolha_curso"] == 'O'):
				discente.motivo_escolha_curso = form.cleaned_data["outro_motivo"]

			if (form.cleaned_data["plano_egresso"] == 'O'):
				discente.plano_egresso = form.cleaned_data["outro_plano"]
			
		discente.save()
		return redirect('discentes_list')
	else:
		mthd = 'g'

		print('discente.motivo_escolha_curso:', discente.motivo_escolha_curso)
		print('discente.plano_egresso:', discente.plano_egresso)
		print('discente.nome_curso_tecnico:', discente.nome_curso_tecnico)
		print('discente.local_curso_tecnico:', discente.local_curso_tecnico)
		print('discente.local_graduacao:', discente.local_graduacao)
		print('discente.nome_graduacao:', discente.nome_graduacao) 

		if((discente.nome_curso_tecnico is not None) and
		 (discente.local_curso_tecnico is not None) and
		 (discente.nome_curso_tecnico != '') and
		 (discente.local_curso_tecnico != '')):
			fct = 'upd_y'
		else:
			fct = 'upd_n'

		if((discente.nome_graduacao is not None) and
			(discente.local_graduacao is not None) and
			(discente.nome_graduacao != '') and
			(discente.local_graduacao != '')):
			fog = 'upd_y'
		else:
			fog = 'upd_n'

		if((discente.projetos_extensao is not None) and (discente.projetos_extensao != '')):
			ppe = 'upd_y'
		else:
			ppe = 'upd_n'

		if((discente.projetos_pesquisa is not None) and (discente.projetos_pesquisa != '')):
			ppp = 'upd_y'
		else:
			ppp = 'upd_n'

		if ((discente.motivo_escolha_curso is not None) and
			(discente.motivo_escolha_curso != '') and
			 	(discente.motivo_escolha_curso != 'F') and
				(discente.motivo_escolha_curso != 'S') and 
				(discente.motivo_escolha_curso != 'N') and
				(discente.motivo_escolha_curso != 'J')):
				om = discente.motivo_escolha_curso
				print('om:', om)
				discente.motivo_escolha_curso = 'O'

		if ((discente.plano_egresso is not None) and
			(discente.plano_egresso != '') and
		 	(discente.plano_egresso != 'A') and
			(discente.plano_egresso != 'F')):
				op = discente.plano_egresso
				discente.plano_egresso = 'O'

		if discente.turno_trabalho is None or discente.turno_trabalho == '':
			tt = 'upd_n'
		else:
			tt = 'upd_y'

		form = DiscenteForm(instance=discente, mthd=mthd, tt=tt, om=om, op=op, fct=fct, fog=fog, ppe=ppe, ppp=ppp)

	return render(request, 'app/discente_new.html', {'form': form})


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

