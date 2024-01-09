import pytest


def test_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Bigger Applications!"}


def test_hello_world(test_client):
    response = test_client.get("/greetings/")
    assert response.json() == "Hello World"


@pytest.mark.parametrize(
    "username,expected",
    [("BuRaK", "Burak"), ("EyUpcAn", "Eyupcan"), ("SEMIR", "Semir"), ("ufuk", "Ufuk")],
)
def test_hello(test_client, username: str, expected: str):
    response = test_client.get(f"/greetings/{username}")
    assert response.json() == f"Hello {expected}"
