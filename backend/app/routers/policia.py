from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.config import CAI_LAYER
from app.utils.gpd_utils import get_layer_data
from app.utils.arcgis_api import get_outfields, get_query_res
from app.utils.folium_maps import generate_map
from app.utils.templates_dir import templates

Policia_Router = APIRouter(prefix='/mapas')

CAI_METADATA    = CAI_LAYER['metadata']
CAI_QUERY       = CAI_LAYER['query']
CAI_PREFIX      = CAI_LAYER['prefixes']

CAI_outfields = get_outfields(CAI_METADATA, CAI_PREFIX)
CAI_response = get_query_res(CAI_QUERY, CAI_outfields, True)
CAI_DATA = get_layer_data(CAI_response)

@Policia_Router.get('/policia')
def map_policia(req: Request):
    """
    Returns a HTML template, where the GeoDataFrame info is displayed as a:
        >>> f_map: Folium interactive map
    """

    f_map = generate_map(
        (CAI_DATA, 
        ['CAIDESCRIP','CAITELEFON', 'CAIIULOCAL', 'CAICELECTR', 'CAIDIR_SIT'],
        ['Descripción', 'Teléfono', 'N° Localidad', 'Correo Electrónico', 'Dirección']
        )
    )

    return templates.TemplateResponse(name='/maps/policia_map.html', request=req, context={'map': f_map})