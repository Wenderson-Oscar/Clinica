from rest_framework import serializers
from medico.models import Medico, Especialidade, Horarios, Agenda

class MedicoSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Medico
        fields = '__all__'  

    
class EspecialidadeSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Especialidade
        fields = '__all__'


class HorariosSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Horarios
        fields = '__all__'


class AgendaSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Agenda
        fields = '__all__'