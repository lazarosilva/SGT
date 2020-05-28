from django.contrib import admin
from .models import Docente, Curso, Disciplina

# Register your models here.

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Docente)