import os

import mercadopago


def _token():
    t = os.environ.get("MERCADOPAGO_ACCESS_TOKEN")
    if not t:
        raise ValueError(
            "Defina MERCADOPAGO_ACCESS_TOKEN no .env (veja .env.example)."
        )
    return t


def criar_pagamento(itens_pedido, link):
    sdk = mercadopago.SDK(_token())

    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome_produto = item.item_estoque.produto.nome
        preco_unitario = float(item.item_estoque.produto.preco)
        itens.append({
            "title": nome_produto,
            "quantity": quantidade,
            "unit_price": preco_unitario,
        })

    preference_data = {
        "items": itens,
        "auto_return": "all",
        "back_urls": {
            "success": link,
            "pending": link,
            "failure": link,
        }
    }
    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta["response"]["init_point"]
    id_pagamento = resposta["response"]["id"]
    return link_pagamento, id_pagamento
