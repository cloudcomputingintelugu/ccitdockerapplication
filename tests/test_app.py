from app import app


def test_home_status_code():
    """
    Verify that the home page returns HTTP 200.
    """
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_home_page_contains_title():
    """
    Verify that the expected page title is present.
    """
    client = app.test_client()

    response = client.get("/")

    assert b"CCIT DevOps Platform" in response.data


def test_home_page_contains_application_name():
    """
    Verify that the application heading is present.
    """
    client = app.test_client()

    response = client.get("/")

    assert b"Cloud Computing in Telugu" in response.data


def test_home_page_contains_kubernetes():
    """
    Verify that Kubernetes information is displayed.
    """
    client = app.test_client()

    response = client.get("/")

    assert b"Kubernetes" in response.data


def test_home_page_contains_argocd():
    """
    Verify that Argo CD information is displayed.
    """
    client = app.test_client()

    response = client.get("/")

    assert b"Argo CD" in response.data


def test_home_page_contains_docker():
    """
    Verify that Docker information is displayed.
    """
    client = app.test_client()

    response = client.get("/")

    assert b"Docker" in response.data


def test_home_page_contains_container_port():
    """
    Verify that the application displays port 5000.
    """
    client = app.test_client()

    response = client.get("/")

    assert b"5000" in response.data