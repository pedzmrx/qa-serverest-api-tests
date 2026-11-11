import requests

BASE_URL = "http://localhost:3000"


def test_listar_usuarios_retorna_200():
    response = requests.get(f"{BASE_URL}/usuarios")

    assert response.status_code == 200
    assert "usuarios" in response.json()