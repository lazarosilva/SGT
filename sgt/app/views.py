from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Curso, Disciplina, Docente, Discente, Tutoria, TutoriaDisciplina, Estagioextracurricular, Atividadecomplementar, Atividadeextracurricular, Estagioextracurricular
from .forms import DisciplinaForm, DocenteForm, DiscenteForm, TutoriaForm, TutoriaDisciplinaForm, AtividadeExtraCurricularForm, AtividadeComplementarForm, EstagioExtraCurricularForm
from django.contrib.auth.models import User, Group


# Create your views here.
@login_required
def index(request):
	return render(request, 'app/index.html')

######################################## CURSOS #############################################

@login_required
def cursos_list(request):
	cursos = Curso.objects.all()
	context = {
		'cursos': cursos
	}
	return render(request, 'app/cursos_list.html', context)

########################################## DISCIPLINAS #######################################

@login_required
def disciplinas_list(request):
	disciplinas = Disciplina.objects.select_related('curso').order_by('curso', 'nome').all()

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


########################################## DOCENTES ###########################################
@login_required
def docentes_list(request):
	docentes = Docente.objects.select_related('curso').order_by('curso', 'nome').all()

	context = {
		'docentes': docentes
	}
	return render(request, 'app/docentes_list.html', context)

@login_required
def docente_new(request):
	if (request.method == 'POST'):
		form = DocenteForm(request.POST, op='add')
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
		form = DocenteForm(op='add')
	return render(request, 'app/docente_new.html', {'form':form})

@login_required
def docente_edit(request, pk):
	docente = get_object_or_404(Docente, pk=pk)	
	if (request.method == 'POST'):
		form = DocenteForm(request.POST, instance=docente, op='upd')
		if (form.is_valid()):
			docente = form.save()
			return redirect('docentes_list')
	else:
		form = DocenteForm(instance=docente, op='upd')
	return render(request, 'app/docente_new.html', {'form': form})

############################################ DISCENTES ########################################

@login_required
def discentes_list(request):
	grupo = request.user.groups.all()[0]
	if grupo.name == 'Coordenador':
		discentes = Discente.objects.select_related('curso').order_by('curso', 'nome').all()
	else:
		tutor = Docente.objects.select_related('curso').filter(email__contains=request.user)
		discentes = Discente.objects.select_related('curso').filter(curso__exact=tutor[0].curso).order_by('curso', 'nome').all()

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

################################## TUTORIAS ####################################

@login_required
def tutorias_list(request):
	tutorias = Tutoria.objects.select_related('discente').all()

	context = {
		'tutorias': tutorias
	}
	return render(request, 'app/tutorias_list.html', context)

@login_required
def tutoria_new(request):
	doc = Docente.objects.select_related('curso').filter(email__exact=request.user.email)
	if (request.method == 'POST'):
		form = TutoriaForm(request.POST, doc=doc)
		if (form.is_valid()):
			tutoria = form.save(commit=False)
			tutoria.docente = doc[0]
			tutoria.save()
			return redirect('tutorias_list')
	else:
		form = TutoriaForm(doc=doc)
	return render(request, 'app/tutoria_new.html', {'form':form})

@login_required
def tutoria_edit(request, pk):
	doc = Docente.objects.filter(email__exact=request.user.email)
	tutoria = get_object_or_404(Tutoria, pk=pk)	
	if (request.method == 'POST'):
		form = TutoriaForm(request.POST, instance=tutoria, doc=doc)
		if (form.is_valid()):
			tutoria = form.save(commit=False)
			tutoria.docente = doc[0]
			tutoria.save()
			return redirect('tutorias_list')
	else:
		form = TutoriaForm(instance=tutoria, doc=doc)
	return render(request, 'app/tutoria_new.html', {'form': form})

@login_required
def tutoria_remove(request, pk):
	tutoria = get_object_or_404(Tutoria, pk=pk)
	tutoria.delete()
	return redirect('tutorias_list')

@login_required
def tutoria_disciplinas_cursadas(request, pk):
	tutoria = get_object_or_404(Tutoria, pk=pk)
	print(tutoria.discente.curso)
	tutoria_disciplina = TutoriaDisciplina.objects.filter(tutoria=tutoria)
	print(tutoria_disciplina is None)
	if tutoria_disciplina:
		retorno = tutoria_disciplinas_cursadas_edit(request, tutoria, tutoria_disciplina)		
	else:
		retorno = tutoria_disciplinas_cursadas_new(request, tutoria)
		return retorno

@login_required
def tutoria_disciplinas_cursadas_new(request, tut):
	if (request.method == 'POST'):
		form = TutoriaDisciplinaForm(request.POST, tut=tut)
		if (form.is_valid()):
			tutoria_disciplina = form.save(commit=False)
			tutoria_disciplina.tutoria = tut[0]
			tutoria.save()
			return redirect('tutorias_list')
	else:
		form = TutoriaDisciplinaForm(tut=tut)
	return render(request, 'app/tutoria_disciplinas_cursadas.html', {'form':form})

@login_required
def tutoria_disciplinas_cursadas_edit(request, tut, tut_disc):
	tutoria_disciplinas_cursadas = tut_disc	
	if (request.method == 'POST'):
		form = TutoriaDisciplinaForm(request.POST, instance=tutoria_disciplinas_cursadas, tut=tut)
		if (form.is_valid()):
			form.save()
			return redirect('tutorias_list')
	else:
		form = TutoriaDisciplinaForm(instance=tutoria_disciplinas_cursadas, tut=tut)
	return render(request, 'app/tutoria_disciplinas_cursadas.html', {'form': form})

################################## ESTÁGIOS EXTRACURRICULARES ################################
@login_required
def tutoria_estagios_list(request, pk):
	tutoria = get_object_or_404(Tutoria, pk=pk)

	estagios = Estagioextracurricular.objects.filter(tutoria=tutoria.id)
	context = {
		'estagios': estagios,
		'tutoria': tutoria
	}
	return render(request, 'app/tutoria_estagios_list.html', context)

@login_required
def tutoria_estagio_new(request, pk):
	tutoria = get_object_or_404(Tutoria, pk=pk)
	if (request.method == 'POST'):
		form = EstagioExtraCurricularForm(request.POST)
		if (form.is_valid()):
			est = form.save(commit=False)
			est.tutoria = tutoria
			est.save()
			return redirect('tutoria_estagios_list', pk=pk)
	else:
		form = EstagioExtraCurricularForm()
	return render(request, 'app/tutoria_estagio_new.html', {'form':form})

@login_required
def tutoria_estagio_edit(request, pk, pk_1):
	tutoria = get_object_or_404(Tutoria, pk=pk)
	estagio = get_object_or_404(Estagioextracurricular, pk=pk_1)
	if (request.method == 'POST'):
		form = EstagioExtraCurricularForm(request.POST, instance=estagio)
		if(form.is_valid()):
			form.save()
			return redirect('tutoria_estagios_list', pk=pk)
	else:
		form = EstagioExtraCurricularForm(instance=estagio)
	return render(request, 'app/tutoria_estagio_new.html', {'form':form})

def tutoria_estagio_remove(request, pk, pk_1):
	estagio = get_object_or_404(Estagioextracurricular, pk=pk_1)
	estagio.delete()
	return redirect('tutoria_estagios_list', pk=pk)

############################### ATIVIDADES EXTRACURRICULARES ################################## 
@login_required
def tutoria_atividades_complementares_list(request, pk):
	tutoria = get_object_or_404(Tutoria, pk=pk)

	acs = Atividadecomplementar.objects.filter(tutoria=tutoria.id)
	context = {
		'acs': acs,
		'tutoria': tutoria
	}
	return render(request, 'app/tutoria_atividades_complementares_list.html', context)

@login_required
def tutoria_atividade_complementar_new(request, pk):
	tutoria = get_object_or_404(Tutoria, pk=pk)
	if (request.method == 'POST'):
		form = AtividadeComplementarForm(request.POST)
		if (form.is_valid()):
			ac = form.save(commit=False)
			ac.tutoria = tutoria
			ac.save()
			return redirect('tutoria_atividades_complementares_list', pk=pk)
	else:
		form = AtividadeComplementarForm()
	return render(request, 'app/tutoria_atividade_complementar_new.html', {'form':form})

@login_required
def tutoria_atividade_complementar_edit(request, pk, pk_1):
	tutoria = get_object_or_404(Tutoria, pk=pk)
	ac = get_object_or_404(Atividadecomplementar, pk=pk_1)
	if (request.method == 'POST'):
		form = AtividadeComplementarForm(request.POST, instance=ac)
		if(form.is_valid()):
			form.save()
			return redirect('tutoria_atividades_complementares_list', pk=pk)
	else:
		form = AtividadeComplementarForm(instance=ac)
	return render(request, 'app/tutoria_atividade_complementar_new.html', {'form':form})

@login_required
def tutoria_atividade_complementar_remove(request, pk, pk_1):
	atividade_complementar = get_object_or_404(Atividadecomplementar, pk=pk_1)
	atividade_complementar.delete()
	return redirect('tutoria_atividades_complementares_list', pk=pk)

############################## ATIVIDADES COMPLEMENTARES #####################################
@login_required
def tutoria_atividades_extracurriculares_list(request, pk):
	tutoria = get_object_or_404(Tutoria, pk=pk)

	aecs = Atividadeextracurricular.objects.filter(tutoria=tutoria.id)
	context = {
		'aecs': aecs,
		'tutoria': tutoria
	}
	return render(request, 'app/tutoria_atividades_extracurriculares_list.html', context)

@login_required
def tutoria_atividade_extracurricular_new(request, pk):
	tutoria = get_object_or_404(Tutoria, pk=pk)
	if (request.method == 'POST'):
		form = AtividadeExtraCurricularForm(request.POST)
		if (form.is_valid()):
			aec = form.save(commit=False)
			aec.tutoria = tutoria
			aec.save()
			return redirect('tutoria_atividades_extracurriculares_list', pk=pk)
	else:
		form = AtividadeExtraCurricularForm()
	return render(request, 'app/tutoria_atividade_extracurricular_new.html', {'form':form})

@login_required
def tutoria_atividade_extracurricular_edit(request, pk, pk_1):
	tutoria = get_object_or_404(Tutoria, pk=pk)
	aec = get_object_or_404(Atividadeextracurricular, pk=pk_1)
	if (request.method == 'POST'):
		form = AtividadeExtraCurricularForm(request.POST, instance=aec)
		if(form.is_valid()):
			form.save()
			return redirect('tutoria_atividades_extracurriculares_list', pk=pk)
	else:
		form = AtividadeExtraCurricularForm(instance=aec)
	return render(request, 'app/tutoria_atividade_extracurricular_new.html', {'form':form})

@login_required
def tutoria_atividade_extracurricular_remove(request, pk, pk_1):
	atividade_extracurricular = get_object_or_404(Atividadeextracurricular, pk=pk_1)
	atividade_extracurricular.delete()
	return redirect('tutoria_atividades_extracurriculares_list', pk=pk)

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

