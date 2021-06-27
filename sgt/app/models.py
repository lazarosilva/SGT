# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Atividadecomplementar(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200)  # Field name made lowercase.
    carga_horaria = models.IntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    tutoria = models.ForeignKey('Tutoria', db_column='TutoriaID', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AtividadeComplementar'


class Atividadeextracurricular(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=10)  # Field name made lowercase.
    bolsista = models.BooleanField(db_column='Bolsista')  # Field name made lowercase.
    tutoria = models.ForeignKey('Tutoria', db_column='TutoriaID', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AtividadeExtraCurricular'


class Curso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    turno = models.CharField(db_column='Turno', max_length=10)  # Field name made lowercase.

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'Curso'


class Discente(models.Model):
    #caracterização inicial
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=200)  # Field name made lowercase.
    nome_social = models.CharField(db_column='NomeSocial', max_length=200, blank=True, null=True)  # Field name made lowercase.
    data_nascimento = models.DateField(db_column='DataNascimento')  # Field name made lowercase.
    genero = models.CharField(db_column='Gênero', max_length=1)  # Field name made lowercase.
    ano_ingresso = models.IntegerField(db_column='AnoIngresso')  # Field name made lowercase.
    natural_de = models.CharField(db_column='CidadeOrigem', max_length=100)  # Field name made lowercase.
    mora_em_serrinha = models.BooleanField(db_column='MoraEmSerrinha', default=True)  # Field name made lowercase.
    coeficiente_de_rendimento = models.FloatField(db_column='CoeficienteRendimento', blank=True, null=True)  # Field name made lowercase.
    semestre_atual = models.IntegerField(db_column='SemestreAtual', blank=True, null=True)  # Field name made lowercase.
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CursoID')  # Field name made lowercase.
    matricula = models.IntegerField(db_column='Matricula')  # Field name made lowercase.
    #caracterização socioeconomica
    turno_trabalho = models.CharField(db_column='TurnoTrabalho', max_length=10, blank=True, null=True)  # Field name made lowercase.
    renda_familiar = models.FloatField(db_column='RendaFamiliar', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tempo_sem_estudar = models.IntegerField(db_column='TempoSemEstudar', blank=True, null=True)  # Field name made lowercase.
    tipo_escola_ens_medio = models.CharField(db_column='TipoEscolaEnsMedio', max_length=20, blank=True, null=True)  # Field name made lowercase.
    #caracterização expectativas
    motivo_escolha_curso = models.CharField(db_column='MotivoEscolhaCurso', max_length=200, blank=True, null=True)  # Field name made lowercase.
    # outro_motivo = models.CharField(db_column='OutroMotivoEscolhaCurso', max_length=200, blank=True, null=True)  # Field name made lowercase. 
    expectativas_curso = models.TextField(db_column='ExpectativasCurso', blank=True, null=True)  # Field name made lowercase.
    sub_areas_interesse = models.TextField(db_column='SubAreasInteresse', blank=True, null=True)  # Field name made lowercase.
    plano_egresso = models.CharField(db_column='PlanoEgresso', max_length=200, blank=True, null=True)  # Field name made lowercase.
    # outro_plano = models.CharField(db_column='OutroPlanoEgresso', max_length=200, blank=True, null=True)  # Field name made lowercase.
    #caracterização experiências e dificuldades
    nome_curso_tecnico = models.CharField(db_column='NomeCursoTecnico', max_length=200, blank=True, null=True)  # Field name made lowercase.
    local_curso_tecnico = models.CharField(db_column='LocalCursoTecnico', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nome_graduacao = models.CharField(db_column='NomeGraduacao', max_length=200, blank=True, null=True)  # Field name made lowercase.
    local_graduacao = models.CharField(db_column='LocalGraduacao', max_length=200, blank=True, null=True)  # Field name made lowercase.
    projetos_extensao = models.TextField(db_column='ProjetoExtensao', blank=True, null=True)  # Field name made lowercase.
    projetos_pesquisa = models.TextField(db_column='ProjetoPesquisa', blank=True, null=True)  # Field name made lowercase.
    dificuldades_ensino_medio = models.TextField(db_column='DificuldadesEnsMedio', blank=True, null=True)  # Field name made lowercase.
    dificuldades_curso = models.TextField(db_column='DificuldadesCurso', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='Ativo', default=True)  # Field name made lowercase.

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'Discente'


class Disciplina(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    carga_horaria = models.IntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    horario_semana = models.CharField(db_column='HorarioSemana', max_length=20, blank=True, null=True)  # Field name made lowercase.
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CursoID')  # Field name made lowercase.
    ativa = models.BooleanField(db_column='Ativa')  # Field name made lowercase.

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'Disciplina'


class Docente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CursoID')  # Field name made lowercase.
    siape = models.IntegerField(db_column='SIAPE')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100)  # Field name made lowercase.

    def __str__(self):
        return self.nome

    class Meta:
        managed = False
        db_table = 'Docente'


class Estagioextracurricular(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100)  # Field name made lowercase.
    remunerado = models.BooleanField(db_column='Remunerado')  # Field name made lowercase.
    carga_horaria = models.IntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    data_inicio = models.DateField(db_column='DataInicio')  # Field name made lowercase.
    data_fim = models.DateField(db_column='DataFim', blank=True, null=True)  # Field name made lowercase.
    tutoria = models.ForeignKey('Tutoria', db_column='TutoriaID', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EstagioExtraCurricular'


class Orientacaomatricula(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='DocenteID')  # Field name made lowercase.
    discente = models.ForeignKey(Discente, models.DO_NOTHING, db_column='DiscenteID')  # Field name made lowercase.
    disciplinas = models.CharField(db_column='Disciplinas', max_length=200, blank=True, null=True)
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OrientacaoMatricula'


# class OrientacaomatriculaDisciplina(models.Model):
#     orientacao = models.ForeignKey(Orientacaomatricula, models.DO_NOTHING, db_column='OrientacaoID')  # Field name made lowercase.
#     disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='DisciplinaID')  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'OrientacaoMatricula_Disciplina'


class Tutoria(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    legislacoes_ifbaiano = models.TextField(db_column='LegislacoesIFBaiano', blank=True, null=True)  # Field name made lowercase.
    dificuldades_semestre_atual = models.TextField(db_column='DificuldadesSemestreAtual', blank=True, null=True)  # Field name made lowercase.
    acoes = models.TextField(db_column='Acoes', blank=True, null=True)  # Field name made lowercase.
    sugestoes_dif_semestre = models.TextField(db_column='SugestoesDifSemestre', blank=True, null=True)  # Field name made lowercase.
    dificuldades_curso = models.TextField(db_column='DificuldadesCurso', blank=True, null=True)  # Field name made lowercase.
    sugestoes_dif_curso = models.TextField(db_column='SugestoesDifCurso', blank=True, null=True)  # Field name made lowercase.
    observacoes = models.TextField(db_column='Observacoes', blank=True, null=True)  # Field name made lowercase.
    docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='DocenteID')  # Field name made lowercase.
    discente = models.ForeignKey(Discente, models.DO_NOTHING, db_column='DiscenteID')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)
    disciplinas_cursadas = models.CharField(db_column='DisciplinasCursadas', max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Tutoria'


class TutoriaDisciplina(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    tutoria = models.ForeignKey(Tutoria, models.DO_NOTHING, db_column='TutoriaID')  # Field name made lowercase.
    disciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='DisciplinaID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tutoria_Disciplina'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
