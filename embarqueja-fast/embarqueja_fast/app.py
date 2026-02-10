from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def leitura():
    return {'message': 'Ola mundo!'}
