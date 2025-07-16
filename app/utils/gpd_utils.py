from geopandas import read_file, GeoDataFrame
from functools import lru_cache

from utils.arcgis_api import fetch_data

def data_to_gdf(api_data):
    """
    Create a GDF from the passed url from the API router
    ----------
    returns:
        GeoDataFrame
    """
    data = fetch_data(api_data, req_dataframe_url=True)
    if data: return read_file(data)

@lru_cache()
def get_layer_data(layer_url):
    """
    Cached GeoDataFrame, avoiding ArcGIS requests overheating
    """
    return data_to_gdf(layer_url) # from URL to geodataframe → data to be manipulated with gpd 