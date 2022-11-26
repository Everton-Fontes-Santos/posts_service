from ninja import NinjaAPI
from ninja.errors import ValidationError
from posts.api import router
from posts.schemas import ErrorSchema
from rich import print

api = NinjaAPI()
api.add_router('',router)

@api.exception_handler(ValidationError)
def custom_validation_errors(request, exc):
    print(exc.errors)  # <--------------------- !!!!
    return api.create_response(request, ErrorSchema(message='Invalid Data'), status=400)