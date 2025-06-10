from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from requests import get, exceptions

from config import DAI_URL, QUERY
from utils.gpd_utils import data_to_gpd
from utils.arcgis_api import fetch_data

DAI_Router = APIRouter()

@DAI_Router.get('/dai')
def get_dai():
    return fetch_data(f'{DAI_URL}{QUERY}')