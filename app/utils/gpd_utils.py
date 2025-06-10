from geopandas import read_file

def data_to_gpd(api_data):
    return read_file(api_data)