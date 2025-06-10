from fastapi import APIRouter, HTTPException
from requests import get, exceptions

def fetch_data(url):
    try:
        data = get(url)
        if data.status_code != 200: #502: Bad Gateway
            raise HTTPException(status_code=502, detail="Error al conectarse con el servidor")
        try:
            return data.json()
        except ValueError as e:
            raise HTTPException(status_code=502, detail=f'Respuesta inválida del servidor: {str(e)}')
    except exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f'Error al obtener datos del servidor: {str(e)}')