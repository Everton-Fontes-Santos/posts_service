from django.test import TestCase
from django.test import Client
from .schemas import HealthCheckSchema, PostSchema, ErrorSchema
from .models import Post
import json

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
        
        self.errorData = json.dumps({
            "title":11,
            "short_text":'This is a simple texto of post',
            "content":'This is a simple text of post, i can do a loren if i want, but not now',
            "author":"oi"
        })
        
    def test_route_healthcheck_return_status_ok(self):
        response = self.client.get('/healthcheck')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            HealthCheckSchema().dict()
        )
    
    def test_route_create_return_status_201(self):
        response = self.client.post('/create',self.succesData.json(), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            self.succesData.dict()
        )
    
    def test_route_create_return_status_400(self):
        response = self.client.post('/create',self.errorData, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            ErrorSchema(message='Invalid Data').dict()
        )
        
    def test_route_retrieve_return_status_200(self): #TODO Fix
        Post.objects.create(**self.succesData.dict())
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            self.succesData.dict()
        )
    
    def test_route_retrieve_return_status_404(self):
        self.client.post('/create',self.succesData.json(), content_type='application/json')
        response = self.client.get('/post/2')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            {'detail':'Not Found'}
        )
        
    def test_route_list_return_status_200(self):
        self.client.post('/create',self.succesData.json(), content_type='application/json')
        response = self.client.get('/list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [self.succesData.dict()]
        )
    def test_route_list_return_status_404(self):
        response = self.client.get('/list')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            ErrorSchema(message='Not Found').dict()
        )