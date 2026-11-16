import requests

def test_listar_usuarios_retorna_200(base_url):
    response = requests.get(f"{base_url}/usuarios")

    assert response.status_code == 200
    assert "usuarios" in response.json()