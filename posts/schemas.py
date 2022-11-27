from pydantic import BaseModel
from typing import List
from ninja import ModelSchema
from .models import Post

class HealthCheckSchema(BaseModel):
    status:str = "ok"
    
class ErrorSchema(BaseModel):
    message:str = "error"
    
class PostSchema(ModelSchema):
    class Config:
        model = Post
        model_fields = '__all__'
        model_exclude = ['created_at']
        
        
class PostIn(BaseModel):
    title:str
    short_text:str
    content:str
    author:int
    
