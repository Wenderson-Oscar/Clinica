from django.db import models
from django.conf import settings

# Create your models here.

class Especialidade(models.Model):

    nome_especialidade = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nome_especialidade


class Medico(models.Model):

    nome = models.CharField(max_length=200, blank=False, null=False)
    crm = models.CharField(max_length=30, unique=True ,blank=False, null=False)
    email = models.EmailField()
    telefone = models.CharField(max_length=17)
    especialidade = models.ForeignKey(Especialidade, on_delete= models.CASCADE, verbose_name="Especialidade", blank=False)

    def __str__(self):
        return self.nome


class Horarios(models.Model):

    horas = models.CharField(max_length=5, blank=False, name=False)

    def __str__(self):
        return self.horas


class Agenda(models.Model):

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name="Médico Especialista", blank=False)
    data = models.DateField()
    horarios = models.ManyToManyField(Horarios, blank=False)

    def __str__(self):
        return self.medico.nome


