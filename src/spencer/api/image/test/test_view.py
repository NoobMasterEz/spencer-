import secrets

from django.contrib.auth.models import User
from django.urls import reverse
from factories.api.image import (CameraFactory, CentroidsFactory,
                                 ImageTransactionFactory)
from factories.test import TestCases
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST,
                                   HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND)

# Create your tests here.


class TestCameraViewSet(TestCases):
    def setUp(self) -> None:
        User.objects.create_superuser(
            'myuser', 'myemail@test.com', '054362770aA')
        self.client.login(username='myuser', password='054362770aA')
        self.camera = CameraFactory()

    def test_camera_method_get_should_connect_200(self):
        response = self.client.get(reverse("camera-list"))
        assert response.status_code == HTTP_200_OK
        assert response.request['PATH_INFO'] == reverse("camera-list")
        assert response.request['REQUEST_METHOD'] == "GET"

    def test_camera_method_get_not_login_should_connect_200(self):
        self.client.logout()
        response = self.client.get(reverse("camera-list"))
        assert response.status_code == HTTP_200_OK
        assert response.json() == [{
            'url': f'http://testserver/api/camera/{self.camera.id}/',
            'name': f'{self.camera.name}',
            'ip': f'{self.camera.ip}'
        }]

    def test_camera_method_get_by_id_should_not_found_key(self):
        response = self.client.get(
            reverse("camera-detail", kwargs={'pk': str(999)}))
        assert response.status_code == HTTP_404_NOT_FOUND
        assert response.json() == {
            'detail':
            'Not found.'
        }

    def test_camera_method_get_by_id_should_connect_200(self):
        response = self.client.get(
            reverse("camera-list"), data={'id': self.camera.id})
        assert response.status_code == HTTP_200_OK
        assert response.data[0]['name'] == self.camera.name
        assert response.data[0]['ip'] == self.camera.ip
        assert response.request['PATH_INFO'] == reverse("camera-list")
        assert response.request['REQUEST_METHOD'] == "GET"

    def test_camera_method_post_should_response_data_corret_and_201(self):
        payload = {
            "name": "test",
            "ip": "192.168.1.1"
        }
        response = self.client.post(reverse("camera-list"), data=payload)
        assert response.status_code == HTTP_201_CREATED
        assert response.data['name'] == payload['name']
        assert response.data['ip'] == payload['ip']

    def test_camera_method_post_not_login_should_can_not_create_and_connect_401(self):
        self.client.logout()
        payload = {
            "name": "test",
            "ip": "192.168.1.1"
        }
        response = self.client.post(reverse("camera-list"), data=payload)
        assert response.status_code == HTTP_401_UNAUTHORIZED
        assert response.json() == {
            'detail':
            'Authentication credentials were not provided.'
        }

    def test_camera_method_patch_should_response_data_corret_and_201(self):
        payload = {
            "name": "test222",
        }
        response = self.client.patch(reverse(
            "camera-list") + f"{self.camera.id}/", data=payload, content_type='application/json')
        assert response.status_code == HTTP_200_OK
        assert response.data['name'] == payload['name']
        assert response.data['ip'] == self.camera.ip

    def test_camera_method_patch_should_not_found_key(self):
        payload = {
            "name": "test222",
        }
        response = self.client.patch(reverse(
            "camera-list") + "99999/", data=payload, content_type='application/json')
        assert response.status_code == HTTP_404_NOT_FOUND
        assert response.json() == {
            'detail':
            'Not found.'
        }

    def test_camera_method_patch_not_login_should_can_not_create_and_connect_401(self):
        self.client.logout()
        payload = {
            "name": "test",
        }
        response = self.client.patch(reverse(
            "camera-list") + f"{self.camera.id}/", data=payload, content_type='application/json')
        assert response.status_code == HTTP_401_UNAUTHORIZED
        assert response.json() == {
            'detail':
            'Authentication credentials were not provided.'
        }

    def test_camera_method_delete_should_return_no_content_204(self):
        response = self.client.delete(reverse("camera-detail", kwargs={"pk": self.camera.id}))
        assert response.status_code == HTTP_204_NO_CONTENT

    def test_camera_method_delete_should_return_not_found_404(self):
        response = self.client.delete(reverse("camera-detail", kwargs={"pk": str(99999)}))
        assert response.status_code == HTTP_404_NOT_FOUND


class TestImageTransactionViewSet(TestCases):
    def setUp(self) -> None:
        User.objects.create_superuser(
            'myuser', 'myemail@test.com', '054362770aA')
        self.client.login(username='myuser', password='054362770aA')
        self.image_transaction = ImageTransactionFactory()

    def test_image_transaction_method_get_should_connect_200(self):
        response = self.client.get(reverse("imagetransaction-list"))
        assert response.status_code == HTTP_200_OK

    def test_image_transaction_method_get_by_id_should_connect_200(self):
        data = {
            'url': f'http://testserver/api/image/{self.image_transaction.id}/',
            'output_base64': f'{self.image_transaction.output_base64}',
            'origin_base64': f'{self.image_transaction.origin_base64}',
            'create_date': f'{self.image_transaction.create_date}',
            'camera': f'http://testserver/api/camera/{self.image_transaction.camera.id}/',
        }
        response = self.client.get(
            reverse("imagetransaction-list"), data={'id': self.image_transaction.id})
        assert response.status_code == HTTP_200_OK
        assert response.json() == [data]

    def test_image_transaction_method_get_by_id_should_not_found_key_and_connect_400(self):
        response = self.client.get(
            reverse("imagetransaction-detail", kwargs={'pk': str(999)}))
        assert response.status_code == HTTP_404_NOT_FOUND
        assert response.json() == {
            'detail':
            'Not found.'
        }

    def test_image_transaction_method_get_not_login_should_connect_200(self):
        self.client.logout()
        response = self.client.get(reverse("imagetransaction-list"))
        assert response.status_code == HTTP_200_OK
        assert response.json()[0]['url'] == f'http://testserver/api/image/{self.image_transaction.id}/'
        assert response.json()[0]['camera'] == f'http://testserver/api/camera/{self.image_transaction.camera.id}/'

    def test_image_transaction_method_post_should_response_data_corret_and_201(self):
        payload = {
            "output_base64": secrets.token_hex(15),
            "origin_base64": secrets.token_hex(15),
            "camera": "http://testserver" + reverse(
                "camera-detail",
                kwargs={
                    'pk': str(self.image_transaction.camera.id)
                })
        }
        response = self.client.post(
            reverse("imagetransaction-list"), data=payload)
        assert response.status_code == HTTP_201_CREATED
        del response.json()['url']
        del response.json()['create_date']
        assert response.json() == payload

    def test_image_transaction_method_post_should_response_not_found_and_404(self):
        payload = {
            "output_base64": secrets.token_hex(15),
            "origin_base64": secrets.token_hex(15),
            "camera": "http://testserver" + reverse(
                "camera-detail",
                kwargs={
                    'pk': str(888888)
                })
        }
        response = self.client.post(
            reverse("imagetransaction-list"), data=payload)
        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.json() == {
            'camera': ['Invalid hyperlink - Object does not exist.']
        }

    def test_image_transaction_method_patch_should_response_data_corret_and_201(self):
        payload = {
            "output_base64": 'test',
        }
        response = self.client.patch(reverse(
            "imagetransaction-list") + f"{self.image_transaction.id}/", data=payload, content_type='application/json')
        assert response.status_code == HTTP_200_OK
        assert response.json()['output_base64'] == payload.get("output_base64", None)

    def test_image_transaction_method_patch_should_response_not_found_and_400(self):
        payload = {
            "output_base64": 'test',
        }
        response = self.client.patch(reverse(
            "imagetransaction-list") + "99999/", data=payload, content_type='application/json')
        assert response.status_code == HTTP_404_NOT_FOUND

    def test_image_transaction_method_delete_should_return_no_content_204(self):
        response = self.client.delete(reverse("imagetransaction-detail", kwargs={"pk": self.image_transaction.id}))
        assert response.status_code == HTTP_204_NO_CONTENT

    def test_image_transaction_method_delete_should_return_not_found_404(self):
        response = self.client.delete(reverse("imagetransaction-detail", kwargs={"pk": str(99999)}))
        assert response.status_code == HTTP_404_NOT_FOUND


class TestCentroidsViewSet(TestCases):
    def setUp(self) -> None:
        User.objects.create_superuser(
            'myuser', 'myemail@test.com', '054362770aA')
        self.client.login(username='myuser', password='054362770aA')
        self.centroids = CentroidsFactory()

    def test_centroid_method_get_should_connect_200(self):
        response = self.client.get(reverse("centroids-list"))
        assert response.status_code == HTTP_200_OK

    def test_centroid_method_get_by_id_should_connect_200(self):
        self.centroids.image_transaction
        data = {
            'url': f'http://testserver/api/centroids/{self.centroids.id}/',
            'x': self.centroids.x,
            'y': self.centroids.y,
            'image_transaction': f'http://testserver/api/image/{self.centroids.image_transaction.id}/',
        }
        response = self.client.get(
            reverse("centroids-list"), data={'id': self.centroids.id})
        assert response.status_code == HTTP_200_OK
        assert response.json() == [data]

    def test_centroid_method_get_by_id_should_not_found_key_and_connect_400(self):
        response = self.client.get(
            reverse("centroids-detail", kwargs={'pk': str(999)}))
        assert response.status_code == HTTP_404_NOT_FOUND
        assert response.json() == {
            'detail':
            'Not found.'
        }

    def test_centroid_method_get_not_login_should_connect_200(self):
        self.client.logout()
        response = self.client.get(reverse("centroids-list"))
        assert response.status_code == HTTP_200_OK
        assert response.json() == [{
            'url': 'http://testserver/api/centroids/8/',
            'x': 7,
            'y': 7,
            'image_transaction': 'http://testserver/api/image/22/',
        }]

    def test_centroid_method_post_should_response_data_corret_and_201(self):
        payload = {
            "x": 11,
            "y": 12,
            "image_transaction": "http://testserver" + reverse(
                "imagetransaction-detail",
                kwargs={
                    'pk': str(self.centroids.image_transaction.id)
                })
        }
        response = self.client.post(
            reverse("centroids-list"), data=payload)
        assert response.status_code == HTTP_201_CREATED
        del response.json()['url']
        assert response.json() == payload

    def test_centroid_method_post_should_response_not_found_and_404(self):
        payload = {
            "x": 11,
            "y": 12,
            "image_transaction": "http://testserver" + reverse(
                "imagetransaction-detail",
                kwargs={
                    'pk': str(888888)
                })
        }
        response = self.client.post(
            reverse("centroids-list"), data=payload)
        assert response.status_code == HTTP_400_BAD_REQUEST
        assert response.json() == {
            'image_transaction': ['Invalid hyperlink - Object does not exist.']
        }

    def test_centroid_method_patch_should_response_data_corret_and_201(self):
        payload = {
            "x": 99,
        }
        response = self.client.patch(reverse(
            "centroids-list") + f"{self.centroids.id}/", data=payload, content_type='application/json')
        assert response.status_code == HTTP_200_OK
        assert response.json()['x'] == payload.get("x", None)

    def test_centroid_method_patch_should_response_not_found_and_400(self):
        payload = {
            "x": 99,
        }
        response = self.client.patch(reverse(
            "centroids-list") + "99999/", data=payload, content_type='application/json')
        assert response.status_code == HTTP_404_NOT_FOUND

    def test_centroid_method_delete_should_return_no_content_204(self):
        response = self.client.delete(reverse("centroids-detail", kwargs={"pk": self.centroids.id}))
        assert response.status_code == HTTP_204_NO_CONTENT

    def test_centroid_method_delete_should_return_not_found_404(self):
        response = self.client.delete(reverse("centroids-detail", kwargs={"pk": str(99999)}))
        assert response.status_code == HTTP_404_NOT_FOUND
