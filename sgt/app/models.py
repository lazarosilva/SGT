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
    cargahoraria = models.IntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    tutoriaid = models.ForeignKey('Tutoria', models.DO_NOTHING, db_column='TutoriaID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AtividadeComplementar'


class Atividadeextracurricular(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=200)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=10)  # Field name made lowercase.
    bolsista = models.IntegerField(db_column='Bolsista')  # Field name made lowercase.
    tutoriaid = models.ForeignKey('Tutoria', models.DO_NOTHING, db_column='TutoriaID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AtividadeExtraCurricular'


class Curso(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    turno = models.CharField(db_column='Turno', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curso'


class Discente(models.Model):
    matricula = models.AutoField(db_column='Matricula', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=200)  # Field name made lowercase.
    nomesocial = models.CharField(db_column='NomeSocial', max_length=200, blank=True, null=True)  # Field name made lowercase.
    datanascimento = models.DateField(db_column='DataNascimento')  # Field name made lowercase.
    gênero = models.CharField(db_column='Gênero', max_length=1)  # Field name made lowercase.
    anoingresso = models.IntegerField(db_column='AnoIngresso')  # Field name made lowercase.
    turnotrabalho = models.CharField(db_column='TurnoTrabalho', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cidadeorigem = models.CharField(db_column='CidadeOrigem', max_length=100)  # Field name made lowercase.
    moraemserrinha = models.IntegerField(db_column='MoraEmSerrinha')  # Field name made lowercase.
    rendafamiliar = models.CharField(db_column='RendaFamiliar', max_length=10)  # Field name made lowercase.
    temposemestudar = models.IntegerField(db_column='TempoSemEstudar', blank=True, null=True)  # Field name made lowercase.
    tipoescolaensmedio = models.CharField(db_column='TipoEscolaEnsMedio', max_length=20)  # Field name made lowercase.
    motivoescolhacurso = models.CharField(db_column='MotivoEscolhaCurso', max_length=200)  # Field name made lowercase.
    expectativascurso = models.TextField(db_column='ExpectativasCurso')  # Field name made lowercase.
    subareasinteresse = models.TextField(db_column='SubAreasInteresse')  # Field name made lowercase.
    planoegresso = models.TextField(db_column='PlanoEgresso')  # Field name made lowercase.
    nomecursotecnico = models.CharField(db_column='NomeCursoTecnico', max_length=200, blank=True, null=True)  # Field name made lowercase.
    localcursotecnico = models.CharField(db_column='LocalCursoTecnico', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nomegraduacao = models.CharField(db_column='NomeGraduacao', max_length=200, blank=True, null=True)  # Field name made lowercase.
    localgraduacao = models.CharField(db_column='LocalGraduacao', max_length=200, blank=True, null=True)  # Field name made lowercase.
    projetoextensao = models.TextField(db_column='ProjetoExtensao', blank=True, null=True)  # Field name made lowercase.
    dificuldadesensmedio = models.TextField(db_column='DificuldadesEnsMedio', blank=True, null=True)  # Field name made lowercase.
    dificuldadescurso = models.TextField(db_column='DificuldadesCurso', blank=True, null=True)  # Field name made lowercase.
    coeficienterendimento = models.FloatField(db_column='CoeficienteRendimento')  # Field name made lowercase.
    semestreatual = models.IntegerField(db_column='SemestreAtual')  # Field name made lowercase.
    cursoid = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CursoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Discente'


class Disciplina(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    cargahoraria = models.IntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    horariosemana = models.CharField(db_column='HorarioSemana', max_length=20)  # Field name made lowercase.
    cursoid = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CursoID')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disciplina'


class Docente(models.Model):
    siape = models.AutoField(db_column='SIAPE', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=100)  # Field name made lowercase.
    perfil = models.CharField(db_column='Perfil', max_length=1)  # Field name made lowercase.
    cursoid = models.ForeignKey(Curso, models.DO_NOTHING, db_column='CursoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Docente'


class Estagioextracurricular(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=100)  # Field name made lowercase.
    remuneracao = models.FloatField(db_column='Remuneracao')  # Field name made lowercase.
    cargahoraria = models.IntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    datainicio = models.DateField(db_column='DataInicio')  # Field name made lowercase.
    datafim = models.DateField(db_column='DataFim', blank=True, null=True)  # Field name made lowercase.
    tutoriaid = models.ForeignKey('Tutoria', models.DO_NOTHING, db_column='TutoriaID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EstagioExtraCurricular'


class Orientacaomatricula(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    docentesiape = models.ForeignKey(Docente, models.DO_NOTHING, db_column='DocenteSIAPE')  # Field name made lowercase.
    discentematricula = models.ForeignKey(Discente, models.DO_NOTHING, db_column='DiscenteMatricula')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrientacaoMatricula'


class OrientacaomatriculaDisciplina(models.Model):
    orientacaoid = models.ForeignKey(Orientacaomatricula, models.DO_NOTHING, db_column='OrientacaoID')  # Field name made lowercase.
    disciplinaid = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='DisciplinaID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrientacaoMatricula_Disciplina'


class Tutoria(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    legislacoesifbaiano = models.TextField(db_column='LegislacoesIFBaiano')  # Field name made lowercase.
    dificuldadessemestreatual = models.TextField(db_column='DificuldadesSemestreAtual')  # Field name made lowercase.
    acoes = models.TextField(db_column='Acoes')  # Field name made lowercase.
    sugestoesdifsemestre = models.TextField(db_column='SugestoesDifSemestre')  # Field name made lowercase.
    dificuldadescurso = models.TextField(db_column='DificuldadesCurso')  # Field name made lowercase.
    sugestoesdifcurso = models.TextField(db_column='SugestoesDifCurso')  # Field name made lowercase.
    observacoes = models.TextField(db_column='Observacoes')  # Field name made lowercase.
    docentesiape = models.ForeignKey(Docente, models.DO_NOTHING, db_column='DocenteSIAPE')  # Field name made lowercase.
    discentematricula = models.ForeignKey(Discente, models.DO_NOTHING, db_column='DiscenteMatricula')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tutoria'


class TutoriaDisciplina(models.Model):
    tutoriaid = models.ForeignKey(Tutoria, models.DO_NOTHING, db_column='TutoriaID')  # Field name made lowercase.
    disciplinaid = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='DisciplinaID')  # Field name made lowercase.

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
