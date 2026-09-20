from fastapi import APIRouter
from app.api.v1 import cifras

base = APIRouter(prefix='/api')

@base.get('/info', include_in_schema=False)
def root():
    return {
        'how to': 'Backend & Data',
        'dev': '@m4tware',
        'logos': 'Proyecto abierto a toda la ciudadanía con fines informativos sobre los hurtos en las diferentes '
                'localidades de Bogotá teniendo en cuenta los puntos de presencia policial distribuidos por la ciudad'
    }

base.include_router(cifras.router, prefix='/cifras')