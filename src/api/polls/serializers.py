from rest_framework import serializers

from .models import Rapper


class RapperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rapper
        fields = ('name', 'aka')
