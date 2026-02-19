from playwright.sync_api import sync_playwright
import time
import json


def test_fluxo_completo_api_serverest():
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url="http://localhost:3000",
            extra_http_headers={
                "Content-Type": "application/json"
            }
        )

        # Cadastro de usuário ADMIN
        email_admin = f"admin_{int(time.time())}@qa.com"

        response_admin = request_context.post(
            "/usuarios",
            data=json.dumps({
                "nome": "Admin",
                "email": email_admin,
                "password": "teste123",
                "administrador": "true"
            })
        )
        print("\n POST /usuarios (admin):")
        print( response_admin.status, response_admin.json())
        assert response_admin.status == 201
        assert response_admin.json()["message"] == "Cadastro realizado com sucesso"

        # Listar usuários Cadastrados
        response_listar = request_context.get("/usuarios")
        print("\n GET /usuarios:")
        print( response_listar.status, response_listar.json())
        assert response_listar.status == 200

        #Buscar usuário por ID
        user_id = response_admin.json()["_id"]
        response_buscar_id = request_context.get(f"/usuarios/{user_id}")
        print(f"\n GET /usuarios/{user_id}:")
        print( response_buscar_id.status, response_buscar_id.json())
        assert response_buscar_id.status == 200
        assert response_buscar_id.json()["_id"] == user_id

        # Editar usuário cadastrado 
        response_editar = request_context.put(
            f"/usuarios/{user_id}",
            data=json.dumps({
                "nome": "Admin Editado",
                "email": email_admin,
                "password": "teste123",
                "administrador": "true"
            })
        )
        print(f"\n PUT /usuarios/{user_id}:")
        print( response_editar.status, response_editar.json())
        assert response_editar.status == 200
        assert response_editar.json()["message"] == "Registro alterado com sucesso"

        # Deletar usuário cadastrado
        response_deletar = request_context.delete(f"/usuarios/{user_id}")
        print(f"\n DELETE /usuarios/{user_id}:")
        print( response_deletar.status, response_deletar.json())
        assert response_deletar.status == 200
        assert response_deletar.json()["message"] == "Registro excluído com sucesso"
