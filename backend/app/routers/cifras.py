from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.config import DAI_LAYER, IRL_LAYER
from app.utils.gpd_utils import get_layer_data, merge_gdf
from app.utils.arcgis_api import get_outfields, get_query_res
from app.utils.folium_maps import generate_map
from app.utils.templates_dir import templates

Cifras_Router = APIRouter(prefix='/mapas')

#TODO: optimize data declaration(maybe a modularization?)
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

CIFRAS_DATA = merge_gdf(DAI_DATA, IRL_DATA, ['CMIULOCAL', 'CMNOMLOCAL'])

# ----- Routers ----- #

@Cifras_Router.get('/delitos', response_class=HTMLResponse, name='map_cifras')
def map_cifras(req: Request):
    """
    Returns a HTML template, where the GeoDataFrame info is displayed as a:
        >>> f_map: Folium interactive map
    """
    CIFRAS = CIFRAS_DATA[CIFRAS_DATA['CMNOMLOCAL'] != 'Sin Localización']

    f_map = generate_map(
        (CIFRAS, 
        ['CMIULOCAL', 'CMNOMLOCAL', 'CMHP25CONT', 'CMH25CONT'], 
        ['N° Localidad', 'Localidad', 'Hurto a Personas - 2025', 'Llamadas por hurto a Personas - 2025']
        )
    )

    return templates.TemplateResponse(name='/maps/cifras_map.html', request=req, context={'map': f_map})

Cifras_stats_Router = APIRouter()

@Cifras_stats_Router.get('/estadisticas', response_class=HTMLResponse, name='stats_cifras')
def stats_cifras(req: Request):
    """
    Returns a HTML template, where the GeoDataFrame info is displayed as a:
        >>> table: GeoDataFrame converted into HTML table with specific classes(Bootstrap friendly)
    """

    chart_data = {
        'Localidad': CIFRAS_DATA['CMNOMLOCAL'].tolist(),
        'N° Localidad': CIFRAS_DATA['CMIULOCAL'].tolist(),
        'Hurtos 2025': CIFRAS_DATA['CMHP25CONT'].tolist(),
        'Llamadas 2025': CIFRAS_DATA['CMH25CONT'].tolist()
    }

    # Calls the GeoDataFrame columns and 
    # assign a readable alias for each one
    cols = CIFRAS_DATA.columns
    aliases = {
        'CMNOMLOCAL': 'Nombre Localidad',
        'CMIULOCAL': 'N° Localidad',
        'CMHP25CONT': 'Hurtos 2025',
        'CMH25CONT': 'Llamadas 2025',
    }

    # Renames the GeoDataFrame columns according to its readable aliases
    CIFRAS = CIFRAS_DATA[cols].rename(columns=aliases)

    table_classes = 'table table-sm table-hover table-striped-columns table-bordered'
    # Drops the geometry, and unused columns for data visualization porpuses
    table = CIFRAS.drop(columns=['geometry', 'CMHPTOTAL', 'CMHTOTAL']).to_html(classes=table_classes, index=False)

    return templates.TemplateResponse(name='/stats/cifras_stats.html', request=req, context={'table': table, 'chart_data': chart_data})

# ----- Routers for Testing Purposes ----- #
""" 
@Cifras_Router.get('/gdf_test')
def stats_cifras(req: Request):
    # Deletes the 'Sin Localización' ; or show also this value?
    #CIFRAS = CIFRAS_DATA[CIFRAS_DATA['CMNOMLOCAL'] != 'Sin Localización']

    chart_map_data = {
        'Localidad': CIFRAS_DATA['CMNOMLOCAL'].tolist(),
        'N° Localidad': CIFRAS_DATA['CMIULOCAL'].tolist(),
        'Hurtos 2025': CIFRAS_DATA['CMHP25CONT'].tolist(),
        'Llamadas 2025': CIFRAS_DATA['CMH25CONT'].tolist()
    }

    print(type(chart_map_data))
    return chart_map_data
 """