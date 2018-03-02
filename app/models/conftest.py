from db import get_connection

import pytest

@pytest.fixture(scope="session")
def conn():
    return get_connection()
