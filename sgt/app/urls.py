from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('cursos/', views.cursos_list, name='cursos_list'),
	path('disciplinas/', views.disciplinas_list, name='disciplinas_list'),
	path('disciplina/new/', views.disciplina_new, name='disciplina_new'),
	path('disciplina/<int:pk>/edit/', views.disciplina_edit, name='disciplina_edit'),
	path('docentes/', views.docentes_list, name='docentes_list'),
	path('docente/new/', views.docente_new, name='docente_new'),
	path('docente/<int:pk>/edit/', views.docente_edit, name='docente_edit'),
]