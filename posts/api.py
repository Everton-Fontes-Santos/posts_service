from ninja import Router
from .schemas import HealthCheckSchema, ErrorSchema
router = Router()

@router.get('healthcheck', response={200: HealthCheckSchema, 403: ErrorSchema})
def healtcheck(request,):
    return HealthCheckSchema()   