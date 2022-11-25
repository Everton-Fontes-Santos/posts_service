from django.test import TestCase
from django.test import Client
from .schemas import HealthCheckSchema
# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        
    def test_route_healthcheck_return_status_ok(self):
        response = self.client.get('/healthcheck')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            HealthCheckSchema().dict()
        )