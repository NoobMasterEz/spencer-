import secrets

import factory
from spencer.api.image.models import Camera, Centroids, ImageTransaction


class CameraFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Camera

    name = factory.Sequence(lambda n: 'john%s' % n)
    ip = factory.Sequence(lambda n: '192.1.1.%s' % n)


class ImageTransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImageTransaction

    output_base64 = factory.Sequence(lambda n: '%s' % secrets.token_hex(15))
    origin_base64 = factory.Sequence(lambda n: '%s' % secrets.token_hex(15))
    create_date = factory.Faker('date_object')
    camera = factory.SubFactory(CameraFactory)


class CentroidsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Centroids

    x = factory.Sequence(lambda n: n)
    y = factory.Sequence(lambda n: n)
    image_transaction = factory.SubFactory(ImageTransactionFactory)
