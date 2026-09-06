from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

#Router Endpoints
from app.routers.cifras import Cifras_Router, api_test#, Cifras_stats_Router
from app.routers.policia import Policia_Router
from app.utils.templates_dir import templates

app = FastAPI(
    title='API GeoData - Bogotá',
    description='Backend de un proyecto abierto a toda la ciudadanía, con fines informativos, sobre los hurtos en las diferentes ' \
                'localidades de Bogotá teniendo en cuenta los puntos de presencia policial distribuidos por la ciudad'
)

app.mount('/app/static', StaticFiles(directory='app/static'), name='static')

app.add_middleware(CORSMiddleware, allow_origins='http://localhost:8001')

@app.get('/info', include_in_schema=False)
def root():
    return {
        'how to': 'Backend & Data',
        'dev': '@m4tware',
        'logos': 'Proyecto abierto a toda la ciudadanía con fines informativos sobre los hurtos en las diferentes '
                'localidades de Bogotá teniendo en cuenta los puntos de presencia policial distribuidos por la ciudad'
    }

@app.get('/', response_class=HTMLResponse, name='home')
def home(req: Request):
    return templates.TemplateResponse(name='home.html', request=req)

app.include_router(Cifras_Router)
# app.include_router(Cifras_stats_Router)
app.include_router(api_test)
app.include_router(Policia_Router)