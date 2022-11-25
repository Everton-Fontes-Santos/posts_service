from pydantic import BaseModel


class HealthCheckSchema(BaseModel):
    status:str = "ok"
    
class ErrorSchema(BaseModel):
    message:str = "error"
