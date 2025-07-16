from folium import Map, Marker, Icon, GeoJson, FeatureGroup, GeoJsonTooltip, LayerControl, TileLayer

def generate_map(*gdf_to_map):
    """
    Each gdf_to_map element must be a tuple:
        >>> (GeoDataFrame, [fields], [aliases], color, layer_name)
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
        * provider Class name also can be used: 
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

    #Marker(
    #    location = [4.65, -74.1],
    #    popup = 'Bogotá',
    #    icon = Icon(color='blue')
    #).add_to(m)

    for gdf, tt_fields, tt_aliases, color, layer_name in gdf_to_map:
        fg = FeatureGroup(name = layer_name)
        GeoJson(
            gdf,
            tooltip = GeoJsonTooltip(fields = tt_fields, aliases = tt_aliases),
            color = color
        ).add_to(fg)
        fg.add_to(m)

    LayerControl(collapsed = False, position = 'bottomright').add_to(m)

    return m._repr_html_()