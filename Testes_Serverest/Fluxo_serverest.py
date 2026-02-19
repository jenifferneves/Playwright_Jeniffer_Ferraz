from playwright.sync_api import sync_playwright
import time
import json


def test_fluxo_completo_api_serverest():
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url="http://localhost:3500",
            extra_http_headers={
                "Content-Type": "application/json"
            }
        )

        # ADMIN
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

        
        # PRODUTO (ADMIN)
        response_produto = request_context.post(
            "/produtos",
            headers=headers_admin,
            data=json.dumps({
                "nome": f"Produto {int(time.time())}",
                "preco": 100,
                "descricao": "Produto teste",
                "quantidade": 5
            })
        )
        print("\n POST /produtos:") 
        print( response_produto.status, response_produto.json())
        assert response_produto.status == 201
        produto_id = response_produto.json()["_id"]
        assert response_produto.json()["message"] == "Cadastro realizado com sucesso"

        
        # CARRINHO (USUÁRIO)
        response_carrinho = request_context.post(
            "/carrinhos",
            headers=headers_user,
            data=json.dumps({
                "produtos": [
                    {
                        "idProduto": produto_id,
                        "quantidade": 1
                    }
                ]
            })
        )
        print("\n POST /carrinhos:")
        print( response_carrinho.status, response_carrinho.json())
        assert response_carrinho.status == 201
        assert response_carrinho.json()["message"] == "Cadastro realizado com sucesso"

        
        # CONCLUIR CARRINHO
        response_concluir = request_context.delete(
            "/carrinhos/concluir-compra",
            headers=headers_user
        )
        print("\n DELETE /carrinhos/ concluir-compra:")
        print( response_concluir.status, response_concluir.json())
        assert response_concluir.status == 200
        assert response_concluir.json()["message"] == "Registro excluído com sucesso"

        
        # DELETAR PRODUTO
        response_delete = request_context.delete(
            f"/produtos/{produto_id}",
            headers=headers_admin
        )
        print(f"\n DELETE /produtos/{produto_id}:")
        print( response_delete.status, response_delete.json())
        assert response_delete.status == 200
        assert response_delete.json()["message"] == "Registro excluído com sucesso"


        # VALIDAR DELETE
        response_get = request_context.get(f"/produtos/{produto_id}")
        print(f"\n GET /produtos/{produto_id} APÓS DELETE:")
        print( response_get.status, response_get.json())
        assert response_get.status == 400
        assert response_get.json()["message"] == "Produto não encontrado"
