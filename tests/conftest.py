import uuid

import pytest

BASE_URL = "http://localhost:3000"


@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def email_unico():
    return f"qa_{uuid.uuid4().hex[:8]}@teste.com"