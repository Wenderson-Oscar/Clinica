from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date

# Create your models here.

class Especialidade(models.Model):

    def validate_name_esp(value: str):
        if not value.isalpha():
            raise ValidationError('Não pode incluir números neste campo.')

    nome_especialidade = models.CharField(max_length=100, blank=False, validators=[validate_name_esp])

    def __str__(self):
        return self.nome_especialidade


class Medico(models.Model):

    def validate_phone(value: str):
        if len(value) < 11:
            raise ValidationError(_('(%(value)s, número errado, deve ter no minimo 11 digitos. '),
            params={'value': value})

    def validate_name(value: str):
        if not value.isalpha():
            raise ValidationError('Não pode incluir números neste campo.')

    nome = models.CharField(max_length=200, blank=False, null=False, validators=[validate_name])
    crm = models.CharField(max_length=30, unique=True ,blank=False, null=False)
    email = models.EmailField()
    telefone = models.CharField(max_length=17, validators=[validate_phone])
    especialidade = models.ForeignKey(Especialidade, on_delete= models.CASCADE, verbose_name="Especialidade", blank=False)

    def __str__(self):
        return self.nome


class Horarios(models.Model):

    horas = models.CharField(max_length=5, blank=False, name=False)

    def __str__(self):
        return self.horas


class Agenda(models.Model):

    def validate_schedule(value: str):
        global data
        data = value
        data_hj = date.today()

        if data < data_hj:
            raise ValidationError('Não é possível selecionar uma data já passada!')

    def validate_medical_schedule(value: str):
        medico = value
        agenda_medico = Agenda.objects.filter(medico__id = medico.id)
        
        for agenda in agenda_medico:
            if data == agenda.data:
                raise ValidationError('Não é possível criar duas agendas na mesma data para um unico médico!')

    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, verbose_name="Médico Especialista", blank=False, validators=[validate_medical_schedule])
    data = models.DateField(validators=[validate_schedule])
    horarios = models.ManyToManyField(Horarios, blank=False)

    def __str__(self):
        return self.medico.nome


