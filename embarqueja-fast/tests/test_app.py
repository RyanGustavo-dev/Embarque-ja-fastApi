from http import HTTPStatus

from fastapi.testclient import TestClient

from embarqueja_fast.app import app

client = TestClient(app)


def test_leitura_deve_retornar_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.json() == {'message': 'Ola mundo!'}
    assert response.status_code == HTTPStatus.OK
