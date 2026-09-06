## ON DEVELOPMENT: 

- New approach:
    - Normal Functioning of [/backend](./backend/):
    - [/frontend](./frontend/) with vanilla JS routing and backend API calls

# FullStack Web App – ArcGIS API geodata Integration & Visualization

Web Data visualization about criminal activity and cop presence in Bogota,
using official geodata from ArcGIS API service.

## Technologies

- Python 3.14
    - pip, venv, uv
- Vite
- Docker
    - docker compose

## Stack

Ensure both services are running, this in order to enable RESTful communication between them

### Backend

- FastAPI
- GeoPandas
- Requests

#### How to run:

- In your local machine, go to [/backend](./backend/)
- Create a virtual env (Python 3.14): using python-venv or uv
- Activate the venv
- Once the venv running, install the [requirements.txt](./backend/requirements.txt)
- Once installed, execute:
    - $ uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
- Using your browser, access to: [http://localhost:8000](http://localhost:8000)

### Frontend

- Vite (Vanilla JS)
- Folium
- Bootsrap CDN
- Chart.JS CDN

#### How to run:

- In your local machine, go to [/frontend](./frontend/)
- Using npm:
    - $ npm run dev --port 8001
- Or if pnpm is preferred:
    - pn run dev --port 8001
