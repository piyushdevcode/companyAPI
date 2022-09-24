from rest_framework.test import APITestCase
from api.models import *


class TestSetUp(APITestCase):
    fixtures = ["test_data.json"]

    def setUp(self):
        self.super_admin = CustomUser.objects.get(username="admin")
        return super().setUp()
