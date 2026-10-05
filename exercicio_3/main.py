from datetime import datetime, date


TAXA_JUROS_DIARIA = 0.025


def calcular_juros(valor, data_vencimento):
    hoje = date.today()

    if data_vencimento >= hoje:
        return 0, 0

    dias_atraso = (hoje - data_vencimento).days
    juros = valor * TAXA_JUROS_DIARIA * dias_atraso

    return dias_atraso, juros


def main():
    try:
        valor = float(
            input("Valor: R$ ").replace(",", ".")
        )

        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")

        vencimento = input("Data de vencimento (DD/MM/AAAA): ")

        data_vencimento = datetime.strptime(
            vencimento,
            "%d/%m/%Y"
        ).date()

        dias_atraso, juros = calcular_juros(
            valor,
            data_vencimento
        )

        valor_total = valor + juros

        print("\nResultado")
        print("-" * 40)
        print(f"Valor original: R$ {valor:.2f}")
        print(f"Dias em atraso: {dias_atraso}")
        print(f"Juros: R$ {juros:.2f}")
        print(f"Valor total: R$ {valor_total:.2f}")

    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()