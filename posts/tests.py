from django.test import TestCase
from django.test import Client
from .schemas import HealthCheckSchema, PostSchema

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.succesData = PostSchema(
            title='A Simple Post',
            short_text='This is a simple texto of post',
            content='This is a simple text of post, i can do a loren if i want, but not now',
            author=1
        )
        
    def test_route_healthcheck_return_status_ok(self):
        response = self.client.get('/healthcheck')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            HealthCheckSchema().dict()
        )
    
    def test_route_create_return_status_ok(self):
        response = self.client.post('/create',)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            HealthCheckSchema().dict()
        )