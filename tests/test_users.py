import requests

def test_listar_usuarios_retorna_200(base_url):
    response = requests.get(f"{base_url}/usuarios")

    assert response.status_code == 200
    assert "usuarios" in response.json()

def test_cadastrar_usuario_com_sucesso(base_url, email_unico):
    payload = {
        "nome": "Usuario QA",
        "email": email_unico,
        "password": "teste123",
        "administrador": "true",
    }

    response = requests.post(f"{base_url}/usuarios", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["message"] == "Cadastro realizado com sucesso"
    assert "_id" in body