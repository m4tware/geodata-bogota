from fastapi import APIRouter, HTTPException
from requests import get, exceptions

def fetch_data(url, req_dataframe = None):
    """
    Define req_dataframe to return a GeoDataFrame if required. Else if JSON defining req_dataframe param is needed
        >>> req_dataframe = 1 → returns a GDF
        >>> req_dataframe = None → returns a JSON
    """
    try:
        data = get(url)
        if data.status_code != 200: #502: Bad Gateway
            raise HTTPException(status_code=502, detail="Error al conectarse con el servidor")
        if req_dataframe is None: # → Returns a JSON format (if required)
            try:
                return data.json()
            except ValueError as e:
                raise HTTPException(status_code=502, detail=f'Respuesta inválida del servidor: {str(e)}')
        return url # → Returns layer fields URL for GeoDataFrame conversion with geopandas
    except exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f'Error al obtener datos del servidor: {str(e)}')