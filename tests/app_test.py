import pytest
import os
import socket

from app import app as flask_app


@pytest.fixture()
def app():
    # other setup can go here
    yield flask_app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_without_env(app, client):
    prefix = "sample"
    hostname = socket.gethostname()

    response = client.get('/')


    assert response.status_code == 200
    assert response.data.decode('utf-8') == str(prefix + ' ' + hostname)