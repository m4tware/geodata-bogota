from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from geopandas import read_file, GeoDataFrame

from config import DAI_LAYER, IRL_LAYER
from utils.gpd_utils import get_layer_data, merge_gdf
from utils.arcgis_api import fetch_data, get_outfields, get_query_res #temp utils, just fot testing
from utils.folium_maps import generate_map
from utils.templates_dir import templates
from utils.plotly_graphs import generate_bar

Cifras_Router = APIRouter(prefix='/cifras')

DAI_METADATA = DAI_LAYER['metadata']
DAI_QUERY    = DAI_LAYER['query']
DAI_PREFIX   = DAI_LAYER['prefixes']

DAI_outfields = get_outfields(DAI_METADATA, DAI_PREFIX)
dai_response = get_query_res(DAI_QUERY, DAI_outfields, True)
DAI_DATA = get_layer_data(dai_response)

IRL_METADATA = IRL_LAYER['metadata']
IRL_QUERY    = IRL_LAYER['query']
IRL_PREFIX   = IRL_LAYER['prefixes']

IRL_outfields = get_outfields(IRL_METADATA, IRL_PREFIX)
irl_response = get_query_res(IRL_QUERY, IRL_outfields, True)
IRL_DATA = get_layer_data(irl_response)

CIFRAS_DATA = merge_gdf(DAI_DATA, IRL_DATA)

@Cifras_Router.get('/mapas', response_class=HTMLResponse, name='map_cifras')
def map_cifras(req: Request):
    """
    Return an HTML template, where the GeoDataFrame info is displayed as a:
    - Folium map
    - Plotly Bar graph object 
    """

    f_map = generate_map(
        (CIFRAS_DATA, 
        ['CMIULOCAL', 'CMNOMLOCAL', 'CMHP25CONT', 'CMH25CONT'], 
        ['N° Localidad', 'Localidad', 'Hurto a Personas - 2025', 'Llamadas por hurto a Personas - 2025'], 
        'gray')
    )

    return templates.TemplateResponse('/maps/cifras_map.html', {'request': req, 'map': f_map})

@Cifras_Router.get('/estadisticas', response_class=HTMLResponse)
def stats_cifras(req: Request):
    return templates.TemplateResponse()

# ----- Routers for Testing Purposes ----- #
@Cifras_Router.get('/dai', name='get_dai')
def get_dai():
    return fetch_data(dai_response) # displaying fetched raw JSON from http request

@Cifras_Router.get('/test_outfields', name='get_dai')
def get_dai():
    outfields = get_outfields(DAI_METADATA, DAI_PREFIX)
    return outfields

@Cifras_Router.get('/test_query', response_class=HTMLResponse, name='get_dai')
def get_dai(req: Request):
    outfields = get_outfields(DAI_METADATA, DAI_PREFIX)
    layer_query_response = get_query_res(DAI_QUERY, outfields, True)
    data = get_layer_data(layer_query_response)

    return templates.TemplateResponse('home.html', {'request': req})