from rest_framework.viewsets import ModelViewSet

from .models import Camera, Centroids, ImageTransaction
from .serializers import (CameraSerializer, CentroidsSerializer,
                          ImageTransactionSerializer)

# Create your views here.


class CameraViewSet(ModelViewSet):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer


class ImageTransactionViewSet(ModelViewSet):
    queryset = ImageTransaction.objects.all()
    serializer_class = ImageTransactionSerializer


class CentroidsViewSet(ModelViewSet):
    queryset = Centroids.objects.all()
    serializer_class = CentroidsSerializer
