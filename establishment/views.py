from rest_framework import viewsets
from serializers import EstablishmentSerializer
from models.establishment import Establishment


class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
