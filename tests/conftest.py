import pytest

from greetings.app import create


@pytest.fixture
def web_client():
    return create().test_client()
