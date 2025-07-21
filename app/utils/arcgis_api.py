from fastapi import APIRouter, HTTPException
from requests import get, exceptions

def fetch_data(url, req_dataframe_url = None):
    """
    Returns a JSON or URL after veryfing a proper connection to ArcGIS API service
    - define req_dataframe_url: to return a GeoDataFrame if required. Else if JSON defining the param is NOT needed
        e.g:
            >>> (url, req_dataframe_url = True) → returns URL for further Query request and GeoDataFrame conversion
            >>> (url) → returns a JSON
    """

    try:
        data = get(url)
        if data.status_code != 200:
            raise HTTPException(status_code=502, detail="Error al conectarse con el servidor") #502: Bad Gateway
        if req_dataframe_url is None: # → Returns a JSON format (if required for fetching API metadata or JSON format query response)
            try:
                return data.json()
            except ValueError as e:
                raise HTTPException(status_code=502, detail=f'Respuesta inválida del servidor: {str(e)}')
        return url # → Returns Layer URL for further GeoDataFrame conversion with geopandas
    except Exception.ValueError as e:
        print(f'Error al obtener los datos:{e}')

def get_outfields(metadata_url, outfields_prefixes):
    """
    Returns a string with the demanded fields from ArcGIS layer
    - url_metadata: url from LAYERS['layer']['metatada']
    - outfields_prefix: first characters of Layer fields
        e.g: CMHP is prefix of: CMHP25CONT, CMHPTOTAL, etc... 
        >>> (LAYERS['layer']['metatada'], 'CMHP')
    """

    #meta = fetch_data(metadata_url)
    meta = get(metadata_url).json()

    fields = [f['name'] for f in meta['fields'] 
            if any(f['name'].startswith(prefix) for prefix in outfields_prefixes)]

    outfields = ",".join(fields + ['CMIULOCAL', 'CMNOMLOCAL'])

    return outfields

def get_query_res(query_url, outfields, geometry):
    """
    Returns the URL with the query and the params according to the data to be fetched from API
    - query_url: url from LAYERS['layer']['query']
    - outfields: data returned from get_outfields()
    - geometry: pass a bool value, True or False, if geometry data is required or not
        e.g:
        >>> (LAYERS['layer']['query'], outfields = get_outfields(), False)
    """

    layer_response = get(query_url, params=dict(where='1=1', 
                                outFields=outfields,
                                f='geojson',
                                returnGeometry=geometry))

    return layer_response.url