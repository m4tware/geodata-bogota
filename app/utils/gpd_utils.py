from geopandas import read_file
from functools import lru_cache

from utils.arcgis_api import fetch_data

def data_to_gpd(api_data):
    """
    Define req_dataframe as True or 1, so fetch_data() returns Layer Fields URL for GeoDataFrame conversion with readfile()
        >>> req_dataframe = True → returns a GDF
    """
    data = fetch_data(api_data, req_dataframe=True)
    return read_file(data)

@lru_cache()
def get_layer_data(layer_url):
    """
    Cached GeoDataFrame, avoiding overheating in ArcGIS requests
    """
    return data_to_gpd(layer_url) # from URL to geodataframe → data to be manipulated with gpd 