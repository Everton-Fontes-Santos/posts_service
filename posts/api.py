from ninja import Router
from . import schemas
from .models import Post
from rich import print
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from typing import List

router = Router()


@router.get('healthcheck', response={200: schemas.HealthCheckSchema, 403: schemas.ErrorSchema})
def healtcheck(request:HttpRequest):
    return schemas.HealthCheckSchema()

@router.post('/create', response={201:schemas.PostSchema, 400: schemas.ErrorSchema})
def create(request, post:schemas.PostIn):
    new_post = Post.objects.create(**post.dict())
    new_post = schemas.PostSchema(**model_to_dict(new_post))
    return 201, new_post

@router.get('/post/{int:id}', response={200: schemas.PostSchema, 404: schemas.ErrorSchema})
def retrieve(request:HttpRequest, id:int):
    
    post = get_object_or_404(Post, id=id)
    response = schemas.PostSchema(**model_to_dict(post))
    return 200, response

    
@router.get('/list', response={200: List[schemas.PostSchema], 404: schemas.ErrorSchema})
def list(request:HttpRequest):
    try:
        posts = Post.objects.all()
        
        if not posts:
            return 404, schemas.ErrorSchema(message="Not Found")
        
        response = [schemas.PostSchema(**model_to_dict(post)) for post in posts]
        return 200, response
    
    except Exception as e:
        return 404, schemas.ErrorSchema(message="Not Found")
    
@router.delete('/delete/{int:id}', response={200: schemas.ErrorSchema, 404: schemas.ErrorSchema})
def delete(request:HttpRequest, id:int):
    try:
        post = get_object_or_404(Post, id=id)
        post.delete()
        return 200, {
                "message":"Success"
            }
    except Exception as e:
        return 404, schemas.ErrorSchema(message="Not Found")
    
@router.put("/update/{id}", response={200:schemas.PostSchema, 400: schemas.ErrorSchema})
def update_post(request, id: int, post: schemas.PostIn):
    try:
        postU = get_object_or_404(Post, id=id)
        for attr, value in post.dict().items():
            setattr(postU, attr, value)
        postU.save()
        return 200, postU
    except Exception as e:
        return 400, schemas.ErrorSchema(message="Invalid Data")