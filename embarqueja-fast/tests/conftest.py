import pytest
from fastapi.testclient import TestClient

from embarqueja_fast.app import app


@pytest.fixture
def client():
    return TestClient(app)
