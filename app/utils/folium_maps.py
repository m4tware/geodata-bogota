from folium import Map, Marker, Icon, GeoJson, FeatureGroup, GeoJsonTooltip, LayerControl

def generate_map(*gdf_to_map):
    """
    Each gdf_to_map element must be a tuple:
        >>> (GeoDataFrame, [fields], [aliases], color, layer_name)
    """
    m = Map(location = [4.65, -74.1], 
        zoom_start = 11.5
    )

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

    LayerControl(collapsed = False).add_to(m)

    return m._repr_html_()