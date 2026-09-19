from fastapi import APIRouter
from app.api.v1 import cifras

base = APIRouter(prefix='/api')

base.include_router(cifras.router, prefix='/cifras')