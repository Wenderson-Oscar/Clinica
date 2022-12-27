from rest_framework import viewsets
from medico.api.serializers import MedicoSerializers, EspecialidadeSerializers, HorariosSerializers, AgendaSerializers
from medico.models import Medico, Especialidade, Horarios, Agenda

class MedicoViewsets(viewsets.ModelViewSet):

    queryset = Medico.objects.all()
    serializer_class = MedicoSerializers


class EspecialidadeViewsets(viewsets.ModelViewSet):

    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializers


class HorariosViewsets(viewsets.ModelViewSet):

    queryset = Horarios.objects.all()
    serializer_class = HorariosSerializers


class AgendaViewsets(viewsets.ModelViewSet):

    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializers