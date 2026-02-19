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

         # USUÁRIO COMUM
        email_user = f"user_{int(time.time())}@qa.com"

        response_user = request_context.post(
            "/usuarios",
            data=json.dumps({
                "nome": "Usuário",
                "email": email_user,
                "password": "teste123",
                "administrador": "false"
            })
        )
        print("\n POST /usuarios (user):")
        print( response_user.status, response_user.json())
        assert response_user.status == 201
        assert response_user.json()["message"] == "Cadastro realizado com sucesso"

        response_login_user = request_context.post(
            "/login",
            data=json.dumps({
                "email": email_user,
                "password": "teste123"
            })
        )
        token_user = response_login_user.json()["authorization"]

        headers_user = {
            "Authorization": token_user
        }
        print("\n POST /login (user):")
        print( response_login_user.status, response_login_user.json())
        assert response_login_user.status == 200
        assert response_login_user.json()["message"] == "Login realizado com sucesso"

        # Listar carrinhos cadastrados
        response_listar = request_context.get("/carrinhos")
        print("\n GET /carrinhos:")
        print( response_listar.status, response_listar.json())
        assert response_listar.status == 200

        # Cadastrar novo carrinho
        response_carrinho = request_context.post(
            "/carrinhos",
            headers=headers_user,
            data=json.dumps({
                "produtos": [
                    {
                        "idProduto": "Rg7G0NZLC8CCt9mK",
                        "quantidade": 2
                    }
                ]
            })
        )
        print("\n POST /carrinhos:")
        print( response_carrinho.status, response_carrinho.json())
        assert response_carrinho.status == 201
        assert response_carrinho.json()["message"] == "Cadastro realizado com sucesso"

        # Buscar carrinho por ID
        carrinho_id = response_carrinho.json()["_id"]
        response_buscar_id = request_context.get(
            f"/carrinhos/{carrinho_id}",
            headers=headers_user
        )
        print(f"\n GET /carrinhos/{carrinho_id}:")
        print( response_buscar_id.status, response_buscar_id.json())
        assert response_buscar_id.status == 200
        assert response_buscar_id.json()["_id"] == carrinho_id

        # Concluir carrinho
        response_concluir = request_context.delete(
            "/carrinhos/concluir-compra",
            headers=headers_user
        )
        print("\n DELETE /carrinhos/concluir-compra:")
        print( response_concluir.status, response_concluir.json())
        assert response_concluir.status == 200
        assert response_concluir.json()["message"] == "Registro excluído com sucesso"

        # Cancelar carrinho (após concluir)
        response_cancelar = request_context.delete(
            "/carrinhos/cancelar-compra",
            headers=headers_user
        )
        print("\n DELETE /carrinhos/cancelar-compra:")
        print( response_cancelar.status, response_cancelar.json())
        assert response_cancelar.status == 200
        assert response_cancelar.json()["message"] == "Não foi encontrado carrinho para esse usuário"

