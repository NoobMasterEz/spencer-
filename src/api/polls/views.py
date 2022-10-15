from rest_framework import viewsets

from .serializers import RapperSerializer
from .models import Rapper


class RapperViewSet(viewsets.ModelViewSet):
    queryset = Rapper.objects.all().order_by('aka')
    serializer_class = RapperSerializer
