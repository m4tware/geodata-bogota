from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

#Router Endpoints
from routers.cifras import Cifras_Router, Cifras_stats_Router
from routers.policia import Policia_Router
from utils.templates_dir import templates

app = FastAPI(
    title='API GeoData - Bogotá',
    description='Backend de un proyecto abierto a toda la ciudadanía, con fines informativos, sobre los hurtos en las diferentes localidades de Bogotá teniendo en cuenta los puntos de presencia policial distribuidos por la ciudad'
)

app.mount('/static', StaticFiles(directory='app/static'), name='static')

@app.get('/', include_in_schema=False)
def root():
    return {
        'how to': 'Backend & Data',
        'dev': '@m4tware',
        'logos': 'Proyecto abierto a toda la ciudadanía con fines informativos sobre los hurtos en las diferentes localidades de Bogotá teniendo en cuenta los puntos de presencia policial distribuidos por la ciudad'
    }

@app.get('/home', response_class=HTMLResponse, name='home')
def home(req: Request):
    return templates.TemplateResponse('home.html', {'request': req})

app.include_router(Cifras_Router)
app.include_router(Cifras_stats_Router)
app.include_router(Policia_Router)