from django.db import models
from django.conf import settings
from medico.models import Agenda
from django.contrib.auth.models import User
# Create your models here.
class Clientes(models.Model):

    SEXO_CHOICES = (
        ('M', 'Maculino'),
        ('F', 'Femenino')
    )

    nome = models.CharField(max_length=200, blank=False, null=False)
    cpf = models.CharField(max_length=14, unique=True ,blank=False, null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    telefone = models.CharField(max_length=16)
    email = models.EmailField()

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    consulta = models.ManyToManyField(Agenda, blank=True)

    def __str__(self):
        return self.nome
