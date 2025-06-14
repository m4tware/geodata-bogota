from fastapi import FastAPI

#Router Endpoints
from routers.cifras import Cifras_Router
from routers.policia import Policia_Router

app = FastAPI(
    title='API GeoData - Bogotá',
    description='Backend de un proyecto abierto a toda la ciudadanía, con fines informativos, sobre los hurtos en las diferentes localidades de Bogotá teniendo en cuenta los puntos de presencia policial distribuidos por la ciudad'
)

@app.get('/')
def root():
    return {
        'how to': 'Data Science',
        'dev': '@m4tware',
        'logos': 'Proyecto abierto a toda la ciudadanía con fines informativos sobre los hurtos en las diferentes localidades de Bogotá teniendo en cuenta los puntos de presencia policial distribuidos por la ciudad'
    }

app.include_router(Cifras_Router)
app.include_router(Policia_Router)