from rest_framework import viewsets
from clientes.api.serializers import ClientesSerializers
from clientes.models import Clientes

class ClientesViewsets(viewsets.ModelViewSet):

    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializers
