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

        # ADMIN TOKEN para cadastro de produto
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

        response_login_admin = request_context.post(
            "/login",
            data=json.dumps({
                "email": email_admin,
                "password": "teste123"
            })
        )
        token_admin = response_login_admin.json()["authorization"]

        headers_admin = {
            "Authorization": token_admin
        }
        print("\n POST /login (admin):")
        print( response_login_admin.status, response_login_admin.json())
        assert response_login_admin.status == 200
        assert response_login_admin.json()["message"] == "Login realizado com sucesso"

        # Listar produtos cadastrados
        response_listar = request_context.get("/produtos")
        print("\n GET /produtos:")
        print( response_listar.status, response_listar.json())
        assert response_listar.status == 200

        # Cadastrar novo produto
        response_cadastrar = request_context.post(
            "/produtos",
            headers=headers_admin,
            data=json.dumps({
                "nome": f"Produto {int(time.time())}",
                "preco": 100,
                "descricao": "Descrição do produto teste",
                "quantidade": 10
            })
        )
        print("\n POST /produtos:") 
        print( response_cadastrar.status, response_cadastrar.json())
        assert response_cadastrar.status == 201
        produto_id = response_cadastrar.json()["_id"]
        assert response_cadastrar.json()["message"] == "Cadastro realizado com sucesso"

        # Buscar produto por ID
        response_buscar_id = request_context.get(f"/produtos/{produto_id}")
        print(f"\n GET /produtos/{produto_id}:")
        print( response_buscar_id.status, response_buscar_id.json())
        assert response_buscar_id.status == 200
        assert response_buscar_id.json()["_id"] == produto_id

        # Editar produto cadastrado
        response_editar = request_context.put(
            f"/produtos/{produto_id}",
            headers=headers_admin,
            data=json.dumps({
                "nome": f"Produto Editado {int(time.time())}",
                "preco": 150,
                "descricao": "Descrição do produto editado",
                "quantidade": 5
            })
        )
        print(f"\n PUT /produtos/{produto_id}:")
        print( response_editar.status, response_editar.json())
        assert response_editar.status == 200
        assert response_editar.json()["message"] == "Registro alterado com sucesso"

        # Deletar produto cadastrado 
        response_deletar = request_context.delete(
            f"/produtos/{produto_id}",
            headers=headers_admin
        )
        print(f"\n DELETE /produtos/{produto_id}:")
        print( response_deletar.status, response_deletar.json())
        assert response_deletar.status == 200
        assert response_deletar.json()["message"] == "Registro excluído com sucesso"
        