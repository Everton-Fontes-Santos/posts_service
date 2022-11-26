from pydantic import BaseModel
from typing import List

class HealthCheckSchema(BaseModel):
    status:str = "ok"
    
class ErrorSchema(BaseModel):
    message:str = "error"
    
class PostSchema(BaseModel):
    title:str
    short_text:str
    content:str
    author:int
    
