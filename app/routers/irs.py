from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from requests import get, exceptions

from config import IRS_URL, QUERY
from utils.arcgis_api import fetch_data

IRS_Router = APIRouter()

@IRS_Router.get('/irs')
def get_irs():
    return fetch_data(f'{IRS_URL}{QUERY}')