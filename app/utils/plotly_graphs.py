from plotly.express import bar

def generate_bar(api_data):
    get_DAI_cols = [col for col in api_data if col.startswith('CMHP') and col.endswith('CONT')]

    years = sorted({2000 + int(col[4:6]) for col in get_DAI_cols})

    fig = bar(api_data, 
            x = 'CMNOMLOCAL', 
            y = get_DAI_cols, 
            barmode = 'group', 
            template = 'plotly_dark',
            labels = {'value': 'Hurto a Personas - (Cifras por Año)', 
                    'CMNOMLOCAL': f'Localidad ({years[-2]} - {years[-1]})', 
                    'variable': 'Cifras Anuales'}) 
        #x = "years [2018,...,2025]", y = "anually data [2018,...,2025]"

    fig.update_layout(showlegend = False)

    return fig.to_html()