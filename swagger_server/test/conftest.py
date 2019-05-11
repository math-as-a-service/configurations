import pytest

from swagger_server.__main__ import app


@pytest.fixture
def client():
    return app.test_client()
