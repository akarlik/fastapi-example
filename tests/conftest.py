import pytest
from fastapi.testclient import TestClient


@pytest.fixture()
def test_client():
    from app.main import get_application

    client = TestClient(get_application())
    yield client
