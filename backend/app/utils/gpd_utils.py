from geopandas import read_file
from functools import lru_cache

from app.utils.arcgis_api import fetch_data

def data_to_gdf(api_data):
    """
    Create a GDF from the passed url from the API router
    ----------
    returns:
        type: GeoDataFrame
    """
    data = fetch_data(api_data, req_dataframe_url=True)
    if data: return read_file(data)

@lru_cache()
def get_layer_data(layer_url):
    """
    Cached GeoDataFrame, avoiding ArcGIS requests overheating
    """
    return data_to_gdf(layer_url) # from URL to geodataframe → data to be manipulated with gpd 

def merge_gdf(base_gdf, extra_gdf, properties):
    """
    Merge two different GeoDataFrames that share common properties such as:
    - ['CMIULOCAL', 'CMNOMLOCAL']: both properties(or ArcGIS fields) share the same values.
    - 'geometry': in some cases, both layers may use the same geometry (this column can be ommitted on: utils.arcgis_api → get_query_res())
    With this, just 1 GeoDataFrame is used for Data Visualization in Folium and Plotly
    e.g:
        >>> (layer_data, extra_layer_data)
    ----------
    returns:
        type: GeoDataFrame
    """
    merging = base_gdf.merge(extra_gdf, on=properties, how='inner', suffixes=['', '_right'])
    merged = merging.drop(columns='geometry_right')

    return merged