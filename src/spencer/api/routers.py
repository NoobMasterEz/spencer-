from rest_framework import routers
from .image.views import (
    ImageTransactionViewSet,
    CameraViewSet,
    CentroidsViewSet)

router = routers.DefaultRouter()
router.register(r'image', ImageTransactionViewSet)
router.register(r'camera', CameraViewSet)
router.register(r'centroids', CentroidsViewSet)
