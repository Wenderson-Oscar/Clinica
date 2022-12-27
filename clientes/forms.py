from django import forms
from clientes.models import Clientes
from medico.models import Agenda
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username']


class ClientesForm(forms.ModelForm):
    
    class Meta:
        model = Clientes
        fields = ('nome','cpf','sexo','telefone','email')

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={ 'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={ 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={ 'class': 'form-control'}),
        }

