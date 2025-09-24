from folium import Map, Marker, Icon, GeoJson, FeatureGroup, GeoJsonTooltip, LayerControl, TileLayer

def generate_map(*gdf_to_map):
    """
    Each gdf_to_map element must be a tuple:
        >>> (GeoDataFrame, [fields], [aliases], color)
    """

    m = Map(
        location = [4.65, -74.1], 
        zoom_start = 11.5,
        tiles = None
    )

    """
    Tiles (BaseMap)
    ---------------
    tiles = 'https://tiles.stadiamaps.com/tiles/alidade_satellite/{z}/{x}/{y}{r}.png'
        * provider Class name also can be used as: 
            >>> tiles = 'Stadia.AlidadeSatellite'
    attr = 'attr string'
    """

    tiles = 'Stadia.AlidadeSatellite'
    attr = '&copy; CNES, Distribution Airbus DS, © Airbus DS, © PlanetObserver (Contains Copernicus Data) | &copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

    TileLayer(
        tiles = tiles,
        attr = attr,
        control = False,
    ).add_to(m)

    for gdf, tt_fields, tt_aliases in gdf_to_map:
        GeoJson(
            gdf,
            tooltip = GeoJsonTooltip(fields = tt_fields, aliases = tt_aliases),
            color = 'cadetblue'
        ).add_to(m)

    return m._repr_html_()