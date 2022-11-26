from pydantic import BaseModel


class HealthCheckSchema(BaseModel):
    status:str = "ok"
    
class ErrorSchema(BaseModel):
    message:str = "error"
    
class PostSchema(BaseModel):
    title:str
    short_text:str
    content:str
    author:int
