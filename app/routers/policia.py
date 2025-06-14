from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from config import CAI_URL, CP_URL, QUERY
from utils.gpd_utils import get_layer_data
from utils.folium_maps import generate_map
from utils.templates_dir import templates
from routers.cifras import DAI_DATA

Policia_Router = APIRouter(prefix='/mapas')

CAI_LAYER = f'{CAI_URL}{QUERY}'
CAI_DATA = get_layer_data(CAI_LAYER)

CP_LAYER = f'{CP_URL}{QUERY}'
CP_DATA = get_layer_data(CP_LAYER)

@Policia_Router.get('/policia', response_class=HTMLResponse)
def map_policia(req: Request):
    f_map = generate_map(
        (CAI_DATA, ['CAINOMBRE'], ['Nombre CAI'], 'green', 'Comandos de Atención Inmediata'),
        (DAI_DATA, ['CMIULOCAL', 'CMNOMLOCAL'], ['Localidad N°', 'Localidad'], 'grey', 'Localidad'),
        (CP_DATA, ['PCUIULOCAL', 'PCUNOMCAI'], ['Localidad N°', 'Nombre CAI'], 'white', ' Cuadrante de Policia')
    )
    return templates.TemplateResponse('policia_map.html', {'request': req, 'map': f_map})