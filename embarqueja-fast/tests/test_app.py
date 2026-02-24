from http import HTTPStatus

from sqlalchemy import select

from embarqueja_fast.Models import User


def test_criar_cliente(client):

    response = client.post(
        '/users',
        json={
            'name': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'name': 'alice',
        'email': 'alice@example.com',
    }


def test_buscar_clientes(client):

    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'name': 'alice',
                'email': 'alice@example.com',
            },
        ]
    }


def test_atualizar_cliente(client):
    response = client.put(
        '/users/1',
        json={
            'name': 'alice2',
            'email': 'alice2@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'id': 1,
        'name': 'alice2',
        'email': 'alice2@example.com',
    }


def test_atualizar_cliente_falho(client):
    response = client.put(
        '/users/0',
        json={
            'name': 'alice2',
            'email': 'alice2@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_buscar_cliente_pelo_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'name': 'alice2',
        'email': 'alice2@example.com',
    }


def test_buscar_cliente_pelo_id_falho(client):
    response = client.get('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_deletar_cliente(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'id': 1,
        'name': 'alice2',
        'email': 'alice2@example.com',
    }


def test_deletar_cliente_falho(client):
    response = client.delete('/users/0')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_create_new_user(session):

    user = User(email='test@email.com', name='testName', password='pass')

    session.add(user)
    session.commit()

    response = session.scalar(select(User).filter(User.email == user.email))

    assert response.name == 'testName'
