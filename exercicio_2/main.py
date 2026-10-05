import json
import uuid
from pathlib import Path


ARQUIVO_ESTOQUE = Path(__file__).parent / "estoque.json"


def carregar_estoque():
    with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["estoque"]


def buscar_produto(produtos, codigo):
    for produto in produtos:
        if produto["codigoProduto"] == codigo:
            return produto

    return None


def movimentar_estoque(produto, tipo, quantidade):
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")

    if tipo == "entrada":
        produto["estoque"] += quantidade
        descricao = f"Entrada de {quantidade} unidade(s)"

    elif tipo == "saida":
        if quantidade > produto["estoque"]:
            raise ValueError("Estoque insuficiente para realizar a saída.")

        produto["estoque"] -= quantidade
        descricao = f"Saída de {quantidade} unidade(s)"

    else:
        raise ValueError("Tipo de movimentação inválido.")

    return {
        "id": str(uuid.uuid4()),
        "descricao": descricao,
        "codigoProduto": produto["codigoProduto"],
        "estoqueFinal": produto["estoque"],
    }


def main():
    produtos = carregar_estoque()

    print("\nProdutos disponíveis")
    print("-" * 50)

    for produto in produtos:
        print(
            f'{produto["codigoProduto"]} - '
            f'{produto["descricaoProduto"]} '
            f'(Estoque: {produto["estoque"]})'
        )

    try:
        codigo = int(input("\nCódigo do produto: "))

        produto = buscar_produto(produtos, codigo)

        if produto is None:
            print("Produto não encontrado.")
            return

        tipo = input("Movimentação (entrada/saida): ").strip().lower()
        quantidade = int(input("Quantidade: "))

        movimentacao = movimentar_estoque(
            produto,
            tipo,
            quantidade,
        )

        print("\nMovimentação realizada com sucesso")
        print("-" * 50)
        print(f'ID: {movimentacao["id"]}')
        print(f'Produto: {produto["descricaoProduto"]}')
        print(f'Descrição: {movimentacao["descricao"]}')
        print(f'Estoque final: {movimentacao["estoqueFinal"]}')

    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()