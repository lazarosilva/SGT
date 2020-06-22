from django.contrib import admin
from .models import Docente, Curso, Disciplina, Discente

# Register your models here.

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Docente)
admin.site.register(Discente)