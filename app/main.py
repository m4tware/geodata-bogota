from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'how to': 'data science'}