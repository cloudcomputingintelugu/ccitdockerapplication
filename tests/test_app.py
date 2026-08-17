import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_home_status_code(client):
    response = client.get("/")

    assert response.status_code == 200


def test_home_page_contains_title(client):
    response = client.get("/")

    assert b"CCIT DevOps Platform-Cloud" in response.data


def test_home_page_contains_application_name(client):
    response = client.get("/")

    assert b"Cloud Computing in Telugu" in response.data


def test_home_page_contains_kubernetes(client):
    response = client.get("/")

    assert b"Kubernetes" in response.data


def test_home_page_contains_argocd(client):
    response = client.get("/")

    assert b"Argo CD" in response.data


def test_home_page_contains_docker(client):
    response = client.get("/")

    assert b"Docker" in response.data


def test_home_page_contains_container_port(client):
    response = client.get("/")

    assert b"5000" in response.data