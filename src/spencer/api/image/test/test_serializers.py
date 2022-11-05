from factories.api.image import (CameraFactory, CentroidsFactory,
                                 ImageTransactionFactory)
from factories.test import TestCases
from rest_framework.exceptions import ErrorDetail

from ..serializers import (CameraSerializer, CentroidsSerializer,
                           ImageTransactionSerializer)


class TestCameraSerializer(TestCases):
    def setUp(self) -> None:
        self.camera_payload = {
            'name': 'test',
            'ip': '192.168.1.1'
        }

    def test_valid_camera_serializer(self):
        camera = CameraSerializer(data=self.camera_payload)

        assert camera.is_valid()
        assert camera.validated_data == self.camera_payload
        assert camera.errors == {}

    def test_invalid_required_camera_serializer(self):
        del self.camera_payload['ip']
        camera = CameraSerializer(data=self.camera_payload)

        assert not camera.is_valid()
        assert camera.validated_data == {}
        assert camera.errors == {
            'ip': [ErrorDetail(string='This field is required.', code='required')]
        }

    def test_invalid_camera_datatype(self):
        camera = CameraSerializer(data=list(self.camera_payload))

        assert not camera.is_valid()
        assert camera.validated_data == {}
        assert camera.errors == {
            'non_field_errors': [
                ErrorDetail(
                    string='Invalid data. Expected a dictionary, but got list.',
                    code='invalid')
            ]
        }


class TestImageTransactionSerializer(TestCases):
    def setUp(self) -> None:
        self.camera = CameraFactory()
        self.image = ImageTransactionFactory(camera=self.camera)
        self.pay_load = {
            'output_base64': self.image.output_base64,
            'origin_base64': self.image.origin_base64,
            'camera': f'http://testserver/api/camera/{self.camera.id}/'
        }

    def test_valid_image_serializer(self):
        image = ImageTransactionSerializer(data=self.pay_load)

        assert image.is_valid()
        assert image.validated_data['output_base64'] == self.image.output_base64
        assert image.validated_data['origin_base64'] == self.image.origin_base64
        assert image.errors == {}

    def test_check_validate_invalid_null_required_image_serializer_should_rais_errors_corret(self):
        self.pay_load['output_base64'] = None
        image = ImageTransactionSerializer(data=self.pay_load)

        assert not image.is_valid()
        assert image.validated_data == {}
        assert image.errors == {
            'output_base64': [ErrorDetail(string='This field may not be null.', code='null')]
        }

    def test_incorrect_type_image_datatype_should_rais_errors_corret(self):
        self.pay_load['camera'] = 1
        image = ImageTransactionSerializer(data=self.pay_load)

        assert not image.is_valid()
        assert image.validated_data == {}
        assert image.errors == {
            'camera': [
                ErrorDetail(
                    string='Incorrect type. Expected URL string, received int.',
                    code='incorrect_type')
            ]
        }


class TestCentroidsSerializer(TestCases):
    def setUp(self) -> None:
        camera = CameraFactory()
        image = ImageTransactionFactory(camera=camera)
        self.centroids = CentroidsFactory(image_transaction=image)
        self.pay_load = {
            'x': self.centroids.x,
            'y': self.centroids.y,
            'image_transaction': f'http://testserver/api/image/{self.centroids.image_transaction.id}/'
        }

    def test_valid_centroids_serializer(self):
        centroids = CentroidsSerializer(data=self.pay_load)

        assert centroids.is_valid()
        assert centroids.validated_data['x'] == self.centroids.x
        assert centroids.validated_data['y'] == self.centroids.y
        assert centroids.errors == {}

    def test_check_validate_invalid_null_required_centroids_serializer_should_rais_errors_corret(self):
        self.pay_load['x'] = None
        centroids = CentroidsSerializer(data=self.pay_load)

        assert not centroids.is_valid()
        assert centroids.validated_data == {}
        assert centroids.errors == {
            'x': [ErrorDetail(string='This field may not be null.', code='null')]
        }

    def test_incorrect_type_image_datatype_should_rais_errors_corret(self):
        self.pay_load['image_transaction'] = 1
        centroids = CentroidsSerializer(data=self.pay_load)

        assert not centroids.is_valid()
        assert centroids.validated_data == {}
        assert centroids.errors == {
            'image_transaction': [
                ErrorDetail(
                    string='Incorrect type. Expected URL string, received int.',
                    code='incorrect_type')
            ]
        }
