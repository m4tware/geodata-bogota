from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from config import DAI_URL, IRL_URL, QUERY
from utils.gpd_utils import get_layer_data
from utils.arcgis_api import fetch_data
from utils.folium_maps import generate_map
from utils.templates_dir import templates

DAI_Router = APIRouter(prefix='/mapas')

LAYER_DAI = f'{DAI_URL}{QUERY}'
DAI_DATA = get_layer_data(LAYER_DAI)

LAYER_IRL = f'{IRL_URL}{QUERY}'
IRL_DATA = get_layer_data(LAYER_IRL)

@DAI_Router.get('/dai', name='get_dai')
def get_dai():
    return fetch_data(LAYER_URL) # displaying fetched raw JSON from http request

@DAI_Router.get('/cifras', response_class=HTMLResponse)
def map_dai(req: Request):
    f_map = generate_map(
        (DAI_DATA, ['CMNOMLOCAL', 'CMHP25CONT'], ['Localidad', ' Hurto a Personas - 2025'], 'green', 'Delitos'),
        (IRL_DATA, ['CMNOMLOCAL', 'CMH25CONT'], ['Localidad', 'Llamadas por Hurto a Personas - 2025'], 'purple', 'Llamadas')
    )
    return templates.TemplateResponse('cifras_map.html', {'request': req, 'mapa': f_map})