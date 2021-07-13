from django import forms
from .models import Curso, Disciplina, TutoriaDisciplina, Docente, Discente, Orientacaomatricula, Tutoria, Atividadecomplementar, Estagioextracurricular, Atividadeextracurricular
from django.core.validators import MaxValueValidator, MinValueValidator 

class DateInput(forms.DateInput):
	input_type = 'date'

class TutoriaDisciplinaForm(forms.ModelForm):
	# tutoria = forms.CharField(required=False, widget=forms.HiddenInput)
	disciplinas = forms.ModelMultipleChoiceField(label='Disciplinas já cursadas', required=False, widget=forms.CheckboxSelectMultiple, queryset=None)
	curso = forms.CharField(label='Curso', required=False)

	class Meta:
		model = TutoriaDisciplina
		fields = ('curso', 'disciplinas')

	def __init__(self, *args, **kwargs):
		self.tut = kwargs.pop('tut')
		super(TutoriaDisciplinaForm, self).__init__(*args, **kwargs)
		# self.fields['docente'].initial = self.doc[0].nome
		# if self.ppp == 'add' or self.ppp == 'upd_n':
		if self.tut != '':
			self.fields['curso'].initial = self.tut.discente.curso
			# self.fields['tutoria'].initial = self.tut
			# self.fields['tutoria'].widget.attrs.update({'selected-option': self.tut.id})
			self.fields['disciplinas'].queryset = Disciplina.objects.filter(curso=self.tut.discente.curso).order_by('nome')

class DisciplinaForm(forms.ModelForm):
	# curso = forms.ModelChoiceField(queryset=Curso.objects.all())
	YES_OR_NO=[(None,'--------'), (True, 'Sim'), (False, 'Não')]
	DIAS_SEMANA=[(2, 'Segunda'), (3, 'Terça'), (4, 'Quarta'), (5, 'Quinta'), (6, 'Sexta'), (7, 'Sábado')]

	carga_horaria = forms.IntegerField(label='Carga Horária')
	carga_horaria.widget.attrs.update({'class': 'hideArrows'})
	ativa = forms.ChoiceField(label='Disciplina Ativa', choices=YES_OR_NO, widget=forms.Select)
	
	horario_semana = forms.MultipleChoiceField(label='Dias da aula', required=False, choices=DIAS_SEMANA, widget=forms.CheckboxSelectMultiple)
	hora_aula_inicio = forms.CharField(label='Início da aula', required=False)
	hora_aula_inicio.widget.attrs.update({'placeholder':'00:00', 'data-mask': '00:00'})
	hora_aula_fim = forms.CharField(label='Fim da aula', required=False)
	hora_aula_fim.widget.attrs.update({'placeholder':'00:00', 'data-mask': '00:00'})

	class Meta:
		model = Disciplina
		fields = ('nome', 'carga_horaria', 'horario_semana', 'hora_aula_inicio', 'hora_aula_fim' , 'curso', 'ativa')


	def __init__(self, *args, **kwargs):
		self.op = kwargs.pop('op')
		self.disc = kwargs.pop('disc')
		super(DisciplinaForm, self).__init__(*args, **kwargs)
		print(self.disc.horario_semana)
		print(self.fields['horario_semana'].choices)
		# print(self.disc.horario_semana)

		lista_horarios_disciplina = []
		for i in self.disc.horario_semana:
			if (i.isnumeric()):
				lista_horarios_disciplina.append(int(i))
		
		print(lista_horarios_disciplina)

		if self.op == 'upd':
			self.fields['horario_semana'].initial = lista_horarios_disciplina

		# self.fields['docente'].required = False
		# self.fields['docente'].widget.attrs.update({'selected-option': self.doc[0].id})
		# self.fields['discente'].queryset = Discente.objects.filter(curso=self.doc[0].curso).order_by('nome')
		# self.fields['horario_semana'].queryset = Disciplina.objects.filter()


class EstagioExtraCurricularForm(forms.ModelForm):
	
	YES_OR_NO=[(None,'--------'), (True, 'Sim'), (False, 'Não')]

	descricao = forms.CharField(max_length=200, label='Descrição')
	carga_horaria = forms.IntegerField(label='Carga Horária')
	carga_horaria.widget.attrs.update({'class': 'hideArrows'})
	data_inicio = forms.DateField(label='Início')
	data_inicio.widget.attrs.update({'data-mask': '00/00/0000'})
	data_fim = forms.DateField(label='Término', required=False)
	data_fim.widget.attrs.update({'data-mask': '00/00/0000'})
	remunerado = forms.ChoiceField(label='Remunerado?', choices=YES_OR_NO, widget=forms.Select)

	class Meta:
		model = Estagioextracurricular
		fields = ('descricao', 'remunerado', 'carga_horaria', 'data_inicio', 'data_fim')

class AtividadeComplementarForm(forms.ModelForm):

	descricao = forms.CharField(max_length=200, label='Descrição')
	carga_horaria = forms.IntegerField(label='Carga Horária')
	carga_horaria.widget.attrs.update({'class': 'hideArrows'})

	class Meta:
		model = Atividadecomplementar
		fields = ('descricao', 'carga_horaria')


class AtividadeExtraCurricularForm(forms.ModelForm):

	TIPO_ATIVIDADE_EC=[(None,'--------'),('ENS','Ensino'), ('PES','Pesquisa'), ('EXT', 'Extensão')]
	YES_OR_NO=[(None,'--------'), (True, 'Sim'), (False, 'Não')]

	descricao = forms.CharField(max_length=200, label='Descrição')
	tipo = forms.ChoiceField(label='Tipo de Atividade', choices=TIPO_ATIVIDADE_EC, widget=forms.Select)
	bolsista = forms.ChoiceField(label='Bolsista?', choices=YES_OR_NO, widget=forms.Select)

	class Meta:
		model = Atividadeextracurricular
		fields = ('descricao', 'tipo', 'bolsista')

class TutoriaForm(forms.ModelForm):

	NO_OR_YES=[('N', 'Não'),('S', 'Sim')]

	# docente = forms.CharField(max_length=200)
	# docente.widget.attrs.update({'disabled': 'disabled'})
	legislacoes_ifbaiano = forms.CharField(label='Você conhece legislações e documentos referentes ao seu curso e ao IF Baiano? Quais?', required=False, widget=forms.Textarea(attrs={'rows': 5}))
	dificuldades_semestre_atual = forms.CharField(label='Quais disciplinas do semestre atual que você está tendo maior dificuldade? Porque?',
     required=False, widget=forms.Textarea(attrs={'rows': 5}))
	acoes = forms.CharField(label='Quais ações você acha que poderiam ajudar nessas disciplinas?', 
     required=False, widget=forms.Textarea(attrs={'rows': 5}))
	sugestoes_dif_semestre = forms.CharField(label='Sugestão(ões) do(a) Tutor(a) para melhorar o rendimento nas disciplinas com dificuldade:',
     required=False, widget=forms.Textarea(attrs={'rows': 5}))
	dificuldades_curso = forms.CharField(label='Qual(is) outra(as) dificuldades você tem enfrentado durante o curso?',
     required=False, widget=forms.Textarea(attrs={'rows': 5}))
	sugestoes_dif_curso = forms.CharField(label='Sugestão(ões) do(a) Tutor(a) para o enfrentamento dessas dificuldades:', 
     required=False, widget=forms.Textarea(attrs={'rows': 5}))
	observacoes = forms.CharField(label='Outras observações do(a) Tutor(a):',
     required=False, widget=forms.Textarea(attrs={'rows': 5}))
	status = forms.ChoiceField(label='Deseja finalizar a tutoria?',
     choices=NO_OR_YES, widget=forms.Select, required=False)
	# docente = forms.ChoiceField(required=False, widget=forms.Select)
	disciplinas_cursadas = forms.ModelMultipleChoiceField(label='Disciplinas já cursadas', required=False, widget=forms.CheckboxSelectMultiple, queryset=None)

	class Meta:
		model = Tutoria
		fields = ('docente', 'discente', 'legislacoes_ifbaiano', 'dificuldades_semestre_atual', 'acoes',
			'sugestoes_dif_semestre', 'dificuldades_curso', 'sugestoes_dif_curso', 'observacoes', 'status', 'disciplinas_cursadas')

	def __init__(self, *args, **kwargs):
		self.doc = kwargs.pop('doc')
		super(TutoriaForm, self).__init__(*args, **kwargs)
		# self.fields['docente'].initial = self.doc[0].nome
		# if self.ppp == 'add' or self.ppp == 'upd_n':
		self.fields['docente'].required = False
		self.fields['docente'].widget.attrs.update({'selected-option': self.doc[0].id})
		self.fields['discente'].queryset = Discente.objects.filter(curso=self.doc[0].curso).order_by('nome')
		self.fields['disciplinas_cursadas'].queryset = Disciplina.objects.filter(curso=self.doc[0].curso).order_by('nome')

class DocenteForm(forms.ModelForm):
	# curso = forms.ModelChoiceField(queryset=Curso.objects.all())
	senha = forms.CharField(max_length=32, widget=forms.PasswordInput)
	email = forms.CharField(max_length=100, label='E-mail')
	siape = forms.IntegerField(label='SIAPE')
	siape.widget.attrs.update({'class': 'hideArrows'}) 
	# confirmar_senha = forms.CharField(max_length=32, widget=forms.PasswordInput)

	# def clean(self):
	#     cleaned_data = super(DocenteForm, self).clean()

	#     password = cleaned_data.get('senha')
	#     password_confirm = cleaned_data.get('confirmar_senha ')

	#     if password and password_confirm:
	#         if password != password_confirm:
	#             raise forms.ValidationError("As senhas não correspondem")
	#     return cleaned_data

	class Meta:
		model = Docente
		fields = ('nome', 'curso', 'email', 'siape',)

	def __init__(self, *args, **kwargs):
		self.op = kwargs.pop('op')
		super(DocenteForm, self).__init__(*args, **kwargs)
		# self.fields['docente'].initial = self.doc[0].nome
		if self.op == 'upd':
			self.fields['senha'].required = False
			self.fields['senha'].widget.attrs.update({'hidePwdField':'S'})

class OrientacaoMatriculaForm(forms.ModelForm):

	NO_OR_YES=[('N', 'Não'),('S', 'Sim')]

	disciplinas = forms.ModelMultipleChoiceField(label='Disciplinas a serem cursadas no próximo semestre', required=False, widget=forms.CheckboxSelectMultiple, queryset=None)
	status = forms.ChoiceField(label='Deseja finalizar a tutoria?',
     choices=NO_OR_YES, widget=forms.Select, required=False)

	class Meta:
		model = Orientacaomatricula
		fields = ('docente', 'discente', 'disciplinas', 'status')

	def __init__(self, *args, **kwargs):
		self.doc = kwargs.pop('doc')
		super(OrientacaoMatriculaForm, self).__init__(*args, **kwargs)
		# self.fields['docente'].initial = self.doc[0].nome
		# if self.ppp == 'add' or self.ppp == 'upd_n':
		self.fields['docente'].required = False
		self.fields['docente'].widget.attrs.update({'selected-option': self.doc[0].id})
		self.fields['discente'].queryset = Discente.objects.filter(curso=self.doc[0].curso).order_by('nome')
		self.fields['disciplinas'].queryset = Disciplina.objects.filter(curso=self.doc[0].curso).order_by('nome')


class DiscenteForm(forms.ModelForm):

	######################################### CONSTANTES #########################################
	GENERO=[(None,'--------'),('M','Masculino'), ('F','Feminino')]
	YES_OR_NO=[(None,'--------'), (True, 'Sim'), (False, 'Não')]
	NO_OR_YES=[('N', 'Não'),('S', 'Sim')]
	TIPO_ESCOLA=[(None,'--------'), ('PUBL','Pública'),('PRIV','Privada'), ('AMBOS', 'Ambos')]
	TURNO_TRABALHO=[(None,'--------'),('D','Diurno'), ('N','Noturno')]

	OPT_MOTIVO_ESCOLHA_CURSO=[(None,'--------'),
						 ('F','Falta de opções melhores'),
						 ('S','Sempre gostei da área'),
						 ('N','Não sabia o que escolher'),
						 ('J','Já trabalho na área'),
						 ('O','Outro motivo')]

	OPT_PLANO_EGRESSO=[(None, '--------'),
						('A','Apenas Trabalhar'),
						('F','Fazer pós-graduação e trabalhar'),
						('O','Outro')]

	OPT_FEZ_OUTRA_GRADUACAO=[('N','Não'), ('S','Sim')]

	####################################################################################################

	data_nascimento = forms.DateField(label='Data de Nascimento')
	data_nascimento.widget.attrs.update({'data-mask': '00/00/0000', 'placeholder': 'dd/mm/aaaa'})

	ano_ingresso = forms.IntegerField(label='Ano de Ingresso')
	ano_ingresso.widget.attrs.update({'class': 'hideArrows'})

	matricula = forms.IntegerField(label='Matrícula')
	matricula.widget.attrs.update({'class': 'hideArrows'})

	coeficiente_de_rendimento = forms.FloatField(label='Coef. Rendimento', required=False, validators=[MinValueValidator(0), MaxValueValidator(10)])
	coeficiente_de_rendimento.widget.attrs.update({'class':'hideArrows', 'placeholder':'0,0'})

	genero = forms.ChoiceField(label='Gênero', choices=GENERO, widget=forms.Select)
	mora_em_serrinha = forms.ChoiceField(label='Mora em Serrinha', choices=YES_OR_NO, widget=forms.Select)
	#mora_em_serrinha = forms.BooleanField(label='Mora em Serrinha', widget=forms.CheckboxInput(attrs={'checked':True}))

	#campos DADOS SOCIOECONOMICOS
	tipo_escola_ens_medio = forms.ChoiceField(label='O Ensino Médio foi em escola', choices=TIPO_ESCOLA, widget=forms.Select, required=False)
	trabalha = forms.ChoiceField(choices=NO_OR_YES, widget=forms.Select, required=False)
	turno_trabalho = forms.ChoiceField(choices=TURNO_TRABALHO, widget=forms.Select , required=False)
	
	# if(op == 'add'):
	# 	turno_trabalho.widget.attrs.update({'disabled': 'disabled'})

	tempo_sem_estudar = forms.IntegerField(label='Tempo sem estudar (em anos)', required=False)
	renda_familiar = forms.IntegerField(label='Renda familiar (em salários mínimos)', required=False)

	#EXPECTATIVAS
	expectativas_curso = forms.CharField(label='Quais as expectativas de aprendizado no curso?', required=False, widget=forms.Textarea(attrs={'rows': 5}))
	sub_areas_interesse = forms.CharField(label='Quais sub-áreas do curso que mais te interessa?', required=False, widget=forms.Textarea(attrs={'rows': 5}))
	motivo_escolha_curso = forms.ChoiceField(label='Por que escolheu esse curso?', required=False, choices=OPT_MOTIVO_ESCOLHA_CURSO, widget=forms.Select)
	outro_motivo = forms.CharField(label='Se marcou outro motivo, descreva-o', max_length=200, required=False)
	plano_egresso = forms.ChoiceField(label='O que pensa em fazer após a graduação:', required=False, choices=OPT_PLANO_EGRESSO, widget=forms.Select)
	outro_plano = forms.CharField(label='Se marcou outro, descreva', max_length=200, required=False)

	#experiências e dificuldades
	fez_curso_tecnico = forms.ChoiceField(label='Fez algum curso técnico?', choices=NO_OR_YES, widget=forms.Select, required=False)
	nome_curso_tecnico = forms.CharField(label='Nome do curso', max_length=100, required=False)
	local_curso_tecnico = forms.CharField(label='Instituição', max_length=100, required=False)
	fez_outra_graduacao = forms.ChoiceField(label='Fez outra graduação (completa ou incompleta)', choices=OPT_FEZ_OUTRA_GRADUACAO, widget=forms.Select, required=False)
	nome_graduacao = forms.CharField(label='Nome do curso', max_length=100, required=False)
	local_graduacao = forms.CharField(label='Instituição' , max_length=100, required=False)
	participou_extensao = forms.ChoiceField(label='Você já participou de projetos de extensão?', choices=NO_OR_YES, widget=forms.Select, required=False)
	projetos_extensao = forms.CharField(label='Se sim, descreva:', required=False, widget=forms.Textarea(attrs={'rows': 5}))
	participou_pesquisa = forms.ChoiceField(label='Você já participou de projetos de pesquisa?', choices=NO_OR_YES, widget=forms.Select, required=False)
	projetos_pesquisa = forms.CharField(label='Se sim, descreva:', required=False, widget=forms.Textarea(attrs={'rows': 5}))

	class Meta:
		model = Discente
		fields = ('nome', 'curso', 'matricula', 'data_nascimento', 'ano_ingresso', 
			'natural_de', 'semestre_atual', 'genero', 'coeficiente_de_rendimento', 
			'mora_em_serrinha', 'tipo_escola_ens_medio', 'trabalha', 'turno_trabalho',
			'tempo_sem_estudar', 'renda_familiar', 'expectativas_curso', 'sub_areas_interesse',
			'motivo_escolha_curso', 'plano_egresso', 'fez_curso_tecnico', 'nome_curso_tecnico',
			'local_curso_tecnico', 'fez_outra_graduacao', 'nome_graduacao', 'local_graduacao', 
			'participou_extensao', 'projetos_extensao','participou_pesquisa', 'projetos_pesquisa',
			'outro_motivo', 'outro_plano')

	def __init__(self, *args, **kwargs):

		self.mthd = kwargs.pop('mthd')
		self.tt = kwargs.pop('tt')
		self.om = kwargs.pop('om')
		self.op = kwargs.pop('op')
		self.fct = kwargs.pop('fct')
		self.fog = kwargs.pop('fog')
		self.ppp = kwargs.pop('ppp')
		self.ppe = kwargs.pop('ppe')

		super(DiscenteForm, self).__init__(*args, **kwargs)

		if self.mthd == 'p':
			return

		if self.ppp == 'add' or self.ppp == 'upd_n':
			self.fields['projetos_pesquisa'].widget.attrs.update({'disabled':'disabled'})
		elif self.ppp == 'upd_y':
			self.fields['participou_pesquisa'].widget.attrs.update({'selected-option': 'S'})

		if self.tt == 'add' or self.tt == 'upd_n':
			self.fields['turno_trabalho'].widget.attrs.update({'disabled': 'disabled'})
		elif self.tt == 'upd_y':
			self.fields['trabalha'].widget.attrs.update({'selected-option': 'S'})

		if self.om != '':
			self.fields['outro_motivo'].initial = self.om
			print('dado OM chegou no campo devido')
		else:
			self.fields['outro_motivo'].widget.attrs.update({'disabled': 'disabled'})

		if self.op != '':
			self.fields['outro_plano'].initial = self.op
		else:
			self.fields['outro_plano'].widget.attrs.update({'disabled': 'disabled'})

		if self.fct == 'add' or self.fct == 'upd_n':
			self.fields['nome_curso_tecnico'].widget.attrs.update({'disabled': 'disabled'})
			self.fields['local_curso_tecnico'].widget.attrs.update({'disabled': 'disabled'})
		elif self.fct == 'upd_y':
			self.fields['fez_curso_tecnico'].widget.attrs.update({'selected-option': 'S'})

		if self.fog == 'add' or self.fog == 'upd_n':
			self.fields['nome_graduacao'].widget.attrs.update({'disabled': 'disabled'})
			self.fields['local_graduacao'].widget.attrs.update({'disabled': 'disabled'})
		elif self.fog == 'upd_y':
			self.fields['fez_outra_graduacao'].widget.attrs.update({'selected-option': 'S'})

		if self.ppe == 'add' or self.ppe == 'upd_n':
			self.fields['projetos_extensao'].widget.attrs.update({'disabled': 'disabled'})
		elif self.ppe == 'upd_y':
			self.fields['participou_extensao'].widget.attrs.update({'selected-option': 'S'})




