ARCGIS_BASE_URL = 'https://oaiee.scj.gov.co/agc/rest/services'

QUERY = '/query?where=1=1&outFields=*&f=geojson'

"""
LAYERS ArcGIS - Tematicos_Pub:
Describe las cifras de los delitos de alto (SIEDCO), 
incidentes 123 (NUSE) y comparendos Ranking (RNMC) 
a nivel de localidad, upz y sector catastral
"""

#DAI: Delitos de Alto Impacto (Por Localidades) - Layer 0
DAI_URL = f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/0'

#IRS: Incidentes Reportados Localidad - Layer 2
IRL_URL = f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/2'

#IRSC: Incidentes Reportados Sector Catastral - Layer 7
IRS_URL = f'{ARCGIS_BASE_URL}/Tematicos_Pub/CifrasSCJ/MapServer/7'

"""
LAYERS ArcGIS - EquipamientoPMSDSCJ:
Estructura y niveles de información del sistema 
de equipamientos para la prestación de los servicios 
de seguridad ciudadana, defensa y justicia.
"""

#CAI: Comando de Atención Inmediata - Layer 22
CAI_URL = f'{ARCGIS_BASE_URL}/Tematicos_NR/EquipamientoPMSDSCJ/MapServer/22'

#CP: Cuadrantes Policia - Layer 25
CP_URL = f'{ARCGIS_BASE_URL}/Tematicos_NR/EquipamientoPMSDSCJ/MapServer/25'

#EQUIP_LOCAL: Equipamientos por Localidad - Layer 28
EQUIP_LOCAL_URL = f'{ARCGIS_BASE_URL}/Tematicos_NR/EquipamientoPMSDSCJ/MapServer/28'

#EQUIP_SC: Equipamientos por Sector Catastral - Layer 30
EQUIP_SC_URL = f'{ARCGIS_BASE_URL}/Tematicos_NR/EquipamientoPMSDSCJ/MapServer/30'