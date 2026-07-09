"""
MODULE POTENTIALLY TO BE DEPRECATED
"""

""" 
from plotly.graph_objects import Figure, Bar

def generate_bar(layer_gdf):
    fig = Figure()

    fig.add_trace(Bar(
        x=[layer_gdf['CMIULOCAL'], layer_gdf['CMNOMLOCAL']],
        y=layer_gdf['CMHP25CONT'],
        name='Delitos 2025',
        marker_color='darkolivegreen',
        hovertemplate='Localidad: %{x}<br>Delitos: %{y}<extra></extra>'
    ))

    fig.add_trace(Bar(
        x=[layer_gdf['CMIULOCAL'], layer_gdf['CMNOMLOCAL']],
        y=layer_gdf['CMH25CONT'],
        name='Llamadas 2025',
        marker_color='darkslateblue',
        hovertemplate='Localidad: %{x}<br>Llamadas: %{y}<extra></extra>'
    ))

    fig.update_layout(
        barmode='group',
        template='plotly_dark',
        title='Delitos vs Llamadas por Localidad (2025)',
        xaxis_title='Nombre y Código de Localidad',
        yaxis_title='',
        showlegend=False,
        dragmode=False
    )

    cfg = {
        "displayModeBar": False,
        "scrollZoom": False,
        "responsive": True
    }

    return fig.to_html(full_html=False, config=cfg) 
"""

# --- Deprecated ---- #
"""
def generate_bar(api_data):
"""
    #Pass the API_DATA from the API Router to fetch its columns for 
    #the corresponding data visualization in a bar chart
"""
    DAI_cols = [col for col in api_data if col.startswith('CMHP') and col.endswith('CONT')]

    years = sorted({2000 + int(col[4:6]) for col in DAI_cols})

    fig = bar(api_data, 
            x = 'CMNOMLOCAL', 
            y = DAI_cols[-2:], 
            color_discrete_sequence = colors.qualitative.Bold, 
            barmode = 'group', 
            template = 'plotly_dark',
            labels = {'value': 'Hurto a Personas - (Cifras por Año)', 
                    'CMIULOCAL': f'Localidad ({years[-2]} - {years[-1]})', 
                    'variable': 'Cifras Anuales'})

    fig.update_layout(showlegend = False, 
                    dragmode = False,
                    margin=dict(l=20, r=20, t=40, b=40),
                    yaxis_title = '')

    cfg = {
        "displayModeBar": False,
        "scrollZoom": False,
        "responsive": True
    }

    return fig.to_html(full_html = False, config = cfg)
"""