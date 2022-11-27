from django.test import TestCase
from django.test import Client
from .schemas import HealthCheckSchema, PostSchema, ErrorSchema, PostIn
from .models import Post
import json

# Create your tests here.
class PostTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.succesData = PostIn(
            title='A Simple Post',
            short_text='This is a simple texto of post',
            content='This is a simple text of post, i can do a loren if i want, but not now',
            author=1
        )
        self.succesResponse = PostSchema(
            id=1,
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
    
    def test_route_list_return_status_404(self):
        response = self.client.get('/list')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            ErrorSchema(message='Not Found').dict()
        )
    
    def test_route_create_return_status_201(self):
        response = self.client.post('/create',self.succesData.json(), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            self.succesResponse.dict()
        )
    
    def test_route_create_return_status_400(self):
        response = self.client.post('/create',self.errorData, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            ErrorSchema(message='Invalid Data').dict()
        )
    
    def test_route_list_return_status_200(self):
        response = self.client.post('/create',self.succesData.json(), content_type='application/json')
        response = self.client.get('/list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            [PostSchema(
            id=3,
            title='A Simple Post',
            short_text='This is a simple texto of post',
            content='This is a simple text of post, i can do a loren if i want, but not now',
            author=1
        ).dict()]
        )
    
    def test_route_retrieve_return_status_200(self):
        post = self.client.post('/create',self.succesData.json(), content_type='application/json')
        response = self.client.get(f'/post/{post.json()["id"]}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            PostSchema(
            id=post.json()["id"],
            title='A Simple Post',
            short_text='This is a simple texto of post',
            content='This is a simple text of post, i can do a loren if i want, but not now',
            author=1
        ).dict()
        )
    
    def test_route_retrieve_return_status_404(self):
        response = self.client.get('/post/3')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            {'detail':'Not Found'}
        )
        
    
    
        
    def test_route_delete_return_status_200(self):
        post = self.client.post('/create',self.succesData.json(), content_type='application/json')
        response = self.client.delete(f'/delete/{post.json()["id"]}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "message":"Success"
            }
        )
    def test_route_delete_return_status_404(self):
        response = self.client.delete('/delete/4')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.json(),
            ErrorSchema(message='Not Found').dict()
        )
        
    def test_route_update_return_status_200(self):
        post = self.client.post('/create',self.succesData.json(), content_type='application/json')
        update = PostIn(
            title='A Simple Post Updated',
            short_text='This is a simple texto of post',
            content='This is a simple text of post, i can do a loren if i want, but not now',
            author=1
        )
        updated = PostSchema(
            id=post.json()["id"],
            title='A Simple Post Updated',
            short_text='This is a simple texto of post',
            content='This is a simple text of post, i can do a loren if i want, but not now',
            author=1
        )
        response = self.client.put(
            f'/update/{post.json()["id"]}',
            update.json(),
            content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            updated.dict()
        )
    
    def test_route_update_return_status_400(self):
        post = self.client.post('/create',self.succesData.json(), content_type='application/json')
        update = PostIn(
            title='A Simple Post Updated',
            short_text='This is a simple texto of post',
            content='This is a simple text of post, i can do a loren if i want, but not now',
            author=1
        )
        response = self.client.put(
            f'/update/{post.json()["id"]+1}',
            update.json(),
            content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            ErrorSchema(message='Invalid Data').dict()
        )