from rest_framework.serializers import HyperlinkedModelSerializer

from .models import ImageTransaction, Centroids, Camera


class CameraSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Camera
        fields = '__all__'


class ImageTransactionSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = ImageTransaction
        fields = '__all__'


class CentroidsSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Centroids
        fields = '__all__'
