import json
from pathlib import Path


ARQUIVO_VENDAS = Path(__file__).parent / "vendas.json"


def carregar_vendas():
    with open(ARQUIVO_VENDAS, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["vendas"]


def calcular_comissao(valor):
    if valor < 100:
        return 0
    elif valor < 500:
        return valor * 0.01
    else:
        return valor * 0.05


def calcular_comissoes(vendas):
    comissoes = {}

    for venda in vendas:
        vendedor = venda["vendedor"]
        valor = venda["valor"]

        comissao = calcular_comissao(valor)

        if vendedor not in comissoes:
            comissoes[vendedor] = 0

        comissoes[vendedor] += comissao

    return comissoes


def exibir_resultados(comissoes):
    print("\nComissões dos vendedores")
    print("-" * 40)

    for vendedor, comissao in comissoes.items():
        print(f"{vendedor}: R$ {comissao:.2f}")


def main():
    vendas = carregar_vendas()
    comissoes = calcular_comissoes(vendas)
    exibir_resultados(comissoes)


if __name__ == "__main__":
    main()