# Loja Django (e-commerce)

Projeto de estudo: vitrine, carrinho (logado ou visitante com cookie), checkout com Mercado Pago, e-mail após pagamento aprovado e uma área interna simples para quem está no grupo `equipe` (números e exportação CSV). O visual copia referência de loja de roupa só para treinar front; não tem ligação comercial com marca nenhuma.

O que o código cobre de verdade: modelagem (pedido, itens, estoque com cor/tamanho, endereço, pagamento), views e templates, autenticação do Django, context processors para carrinho e menu, e integração com API do Mercado Pago via variável de ambiente.

## Antes de rodar

- Python 3.10+
- Instalar dependências: `pip install -r requirements.txt`
- Copiar `.env.example` para `.env` e preencher pelo menos `SECRET_KEY`. Para testar pagamento, coloque `MERCADOPAGO_ACCESS_TOKEN` (token de teste da sua conta Mercado Pago). E-mail: se não configurar SMTP, o Django manda o texto do e-mail para o console.

```bash
copy .env.example .env
python manage.py migrate
python manage.py runserver
```

Abre em `http://127.0.0.1:8000/`. Superusuário: `python manage.py createsuperuser` e acessa `/admin/`.

## Pastas

- `ecommerce/` — `settings`, `urls` do projeto, WSGI.
- `loja/` — app principal: `models`, `views`, `urls`, `utils` (filtros, CSV, e-mail), `api_mercadopago.py`, `novos_context.py` (carrinho no template), templates em `templates/` (inclui `usuario/` e `interno/`).
- `static/` — CSS, JS e imagens servidos em desenvolvimento.

Não suba o `.env` nem o `db.sqlite3` para o Git (já estão no `.gitignore`). Chaves e senhas ficam só na sua máquina ou no servidor.

## Licença

Uso livre para aprender e adaptar.
