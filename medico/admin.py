from django.contrib import admin
from medico.models import Medico, Especialidade, Horarios, Agenda

# Register your models here.
admin.site.register(Medico)
admin.site.register(Especialidade)
admin.site.register(Horarios)
admin.site.register(Agenda)

