from ninja import NinjaAPI
from posts.api import router

api = NinjaAPI()
api.add_router('',router)