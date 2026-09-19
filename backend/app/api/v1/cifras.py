from fastapi import APIRouter, HTTPException
from httpx import AsyncClient

from app.config import DAI_LAYER
from app.utils.arcgis_api import get_outfields, get_query_res

DAI_METADATA = DAI_LAYER['metadata']
DAI_QUERY    = DAI_LAYER['query']
DAI_PREFIX   = DAI_LAYER['prefixes']

DAI_outfields = get_outfields(DAI_METADATA, DAI_PREFIX)
dai_response = get_query_res(DAI_QUERY, DAI_outfields, True)

router = APIRouter()

@router.get('/delitos-alto-impacto/geojson')
async def get_cifras_geojson():
    try:
        async with AsyncClient() as client:
            data = await client.get(dai_response)
            return data.json()
    except:
        raise HTTPException(status_code=404, detail="resource not found")