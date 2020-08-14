from django.urls import path
from . import views


# app_name = "app" 

urlpatterns = [
	path('', views.index, name='index'),
	path('senha/', views.change_password, name='change_password'),
	path('password_reset/', views.password_reset_request, name='password_reset'),
	path('cursos/', views.cursos_list, name='cursos_list'),
	path('disciplinas/', views.disciplinas_list, name='disciplinas_list'),
	path('disciplina/new/', views.disciplina_new, name='disciplina_new'),
	path('disciplina/<int:pk>/edit/', views.disciplina_edit, name='disciplina_edit'),
	path('docentes/', views.docentes_list, name='docentes_list'),
	path('docente/new/', views.docente_new, name='docente_new'),
	path('docente/<int:pk>/edit/', views.docente_edit, name='docente_edit'),
	path('discentes/', views.discentes_list, name='discentes_list'),
	path('discente/new/', views.discente_new, name='discente_new'),
	path('discente/<int:pk>/edit/', views.discente_edit, name='discente_edit'),
	path('tutorias/', views.tutorias_list, name='tutorias_list'),
	path('tutoria/new/', views.tutoria_new, name='tutoria_new'),
	path('tutoria/<int:pk>/edit/', views.tutoria_edit, name='tutoria_edit'),
	path('tutoria/<int:pk>/remove/', views.tutoria_remove, name='tutoria_remove'),
	# path('tutoria/<int:pk>/disciplinas_cursadas/', views.tutoria_disciplinas_cursadas, name='tutoria_disciplinas_cursadas'),
	path('tutoria/<int:pk>/estagios/', views.tutoria_estagios_list, name='tutoria_estagios_list'),
	path('tutoria/<int:pk>/estagios/new', views.tutoria_estagio_new, name='tutoria_estagio_new'),
	path('tutoria/<int:pk>/estagios/<int:pk_1>/edit', views.tutoria_estagio_edit, name='tutoria_estagio_edit'),	
	path('tutoria/<int:pk>/estagios/<int:pk_1>/remove', views.tutoria_estagio_remove, name='tutoria_estagio_remove'),	
	path('tutoria/<int:pk>/atividades_complementares/', views.tutoria_atividades_complementares_list, name='tutoria_atividades_complementares_list'),
	path('tutoria/<int:pk>/atividades_complementares/new', views.tutoria_atividade_complementar_new, name='tutoria_atividade_complementar_new'),	
	path('tutoria/<int:pk>/atividades_complementares/<int:pk_1>/edit', views.tutoria_atividade_complementar_edit, name='tutoria_atividade_complementar_edit'),	
	path('tutoria/<int:pk>/atividades_complementares/<int:pk_1>/remove', views.tutoria_atividade_complementar_remove, name='tutoria_atividade_complementar_remove'),	
	path('tutoria/<int:pk>/atividades_extracurriculares/', views.tutoria_atividades_extracurriculares_list, name='tutoria_atividades_extracurriculares_list'),
	path('tutoria/<int:pk>/atividades_extracurriculares/new', views.tutoria_atividade_extracurricular_new, name='tutoria_atividade_extracurricular_new'),
	path('tutoria/<int:pk>/atividades_extracurriculares/<int:pk_1>/edit', views.tutoria_atividade_extracurricular_edit, name='tutoria_atividade_extracurricular_edit'),	
	path('tutoria/<int:pk>/atividades_extracurriculares/<int:pk_1>/remove', views.tutoria_atividade_extracurricular_remove, name='tutoria_atividade_extracurricular_remove'),	
	path('orientacoes_matricula/', views.orientacoes_matricula_list, name='orientacoes_matricula_list'),
	path('orientacoes_matricula/new/', views.orientacao_matricula_new, name='orientacao_matricula_new'),
	path('orientacoes_matricula/<int:pk>/edit/', views.orientacao_matricula_edit, name='orientacao_matricula_edit'),
]