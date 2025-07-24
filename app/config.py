ARCGIS_BASE_URL = 'https://oaiee.scj.gov.co/agc/rest/services'

DAI_LAYER = {
    """
    Delitos de Alto Impacto (Por Localidades) - Layer 0
    """
    'url':      f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/0',
    'metadata': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/0?f=json',
    'query':    f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/0/query?',
    'prefixes':   ['CMIULOCAL', 'CMNOMLOCAL', 'CMHP25', 'CMHPTOTAL']
    }

IRL_LAYER = {
    """
    Incidentes Reportados Localidad - Layer 2        
    """
    'url':      f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/2',
    'metadata': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/2?f=json',
    'query':    f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/2/query?',
    'prefixes':   ['CMIULOCAL', 'CMNOMLOCAL', 'CMH25', 'CMHTOTAL']
    }

CAI_LAYER = {
    """
    Comando de Atención Inmediata - Layer 22       
    """
    'url':      f'{ARCGIS_BASE_URL}Tematicos_NR/EquipamientoPMSDSCJ/MapServer/22',
    'metadata': f'{ARCGIS_BASE_URL}Tematicos_NR/EquipamientoPMSDSCJ/MapServer/22?f=json',
    'query':    f'{ARCGIS_BASE_URL}Tematicos_NR/EquipamientoPMSDSCJ/MapServer/22/query?',
    'prefixes':   ['CAIIULOCAL', 'CAIDESCRIP', 'CAITELEFON', 'CAICELECTR', 'CAIDIR_SIT']
    }

"""
LAYERS ArcGIS - Tematicos_Pub:
Describe las cifras de los delitos de alto (SIEDCO), 
incidentes 123 (NUSE) y comparendos Ranking (RNMC) 
a nivel de localidad, upz y sector catastral
"""

#DAI: Delitos de Alto Impacto (Por Localidades) - Layer 0
DAI_URL = f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/0'
"""
DAI: 
Delitos de Alto Impacto (Por Localidades) - Layer 0
"""

IRL_URL = f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/2'
"""
IRS: 
Incidentes Reportados Localidad - Layer 2
"""

IRS_URL = f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/7'
"""
IRSC: 
Incidentes Reportados Sector Catastral - Layer 7
"""

"""
LAYERS ArcGIS - EquipamientoPMSDSCJ:
Estructura y niveles de información del sistema 
de equipamientos para la prestación de los servicios 
de seguridad ciudadana, defensa y justicia.
"""

CAI_URL = f'{ARCGIS_BASE_URL}/Tematicos_NR/EquipamientoPMSDSCJ/MapServer/22'
"""
CAI: 
Comando de Atención Inmediata - Layer 22
"""

CP_URL = f'{ARCGIS_BASE_URL}/Tematicos_NR/EquipamientoPMSDSCJ/MapServer/25'
"""
CP: 
Cuadrantes Policia - Layer 25
"""

EQUIP_LOCAL_URL = f'{ARCGIS_BASE_URL}/Tematicos_NR/EquipamientoPMSDSCJ/MapServer/28'
"""
EQUIP_LOCAL: 
Equipamientos por Localidad - Layer 28
"""

EQUIP_SC_URL = f'{ARCGIS_BASE_URL}/Tematicos_NR/EquipamientoPMSDSCJ/MapServer/30'
"""
EQUIP_SC: 
Equipamientos por Sector Catastral - Layer 30
"""

QUERY = '/query?where=1=1&outFields=CMIULOCAL,CMNOMLOCAL,CMHP25CONT&f=geojson'

# ----- Temp Global Dict -----#
""" LAYERS = {
    'DAI': {
        #Delitos de Alto Impacto (Por Localidades) - Layer 0
        'url': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/0',
        'metadata': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/0?f=json',
        'query': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/0/query?'
    },
    'IRL': {
        #Incidentes Reportados Localidad - Layer 2
        'url': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/2',
        'metadata': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/0?f=json',
        'query': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/0/query?'
    },
    'CAI': {
        #Comando de Atención Inmediata - Layer 22
        'url': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/22',
        'metadata': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/22?f=json',
        'query': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/22/query?'
    },
    'CP': {
        #Cuadrantes Policia - Layer 25
        'url': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/25',
        'metadata': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/25?f=json',
        'query': f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/25/query?'
    }
} """