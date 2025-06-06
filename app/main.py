from fastapi import FastAPI

app = FastAPI(
    title='API para Visualización de Datos (Hurtos y Presencia Policial) en Bogotá',
    description='Backend de un proyecto abierto a toda la ciudadanía, con fines informativos, sobre los hurtos en las diferentes localidades de Bogotá teniendo en cuenta los puntos de presencia policial distribuidos por la ciudad'
)

@app.get('/')
def root():
    return {
        'how to': 'Data Science',
        'dev': '@m4tware',
        'logos': 'Proyecto abierto a toda la ciudadanía con fines informativos sobre los hurtos en las diferentes localidades de Bogotá teniendo en cuenta los puntos de presencia policial distribuidos por la ciudad'
    }