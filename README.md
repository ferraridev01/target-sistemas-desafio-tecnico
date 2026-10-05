# Desafio Técnico - Target Sistemas

Solução desenvolvida para o desafio técnico do processo seletivo da Target Sistemas para a vaga de Desenvolvedor(a) de Sistemas Jr.

O projeto foi desenvolvido em Python e contém três exercícios independentes envolvendo lógica de programação, manipulação de JSON, controle de estoque e cálculo de juros.

## Estrutura do projeto

```text
target-sistemas-desafio-tecnico/
├── exercicio_1/
│   ├── main.py
│   └── vendas.json
├── exercicio_2/
│   ├── main.py
│   └── estoque.json
├── exercicio_3/
│   └── main.py
├── .gitignore
└── README.md
```

## Exercício 1 - Comissão de vendedores

O programa lê os registros de vendas presentes em `vendas.json` e calcula a comissão total de cada vendedor.

Regras utilizadas para cada venda:

* Venda abaixo de R$ 100,00: sem comissão.
* Venda de R$ 100,00 até R$ 499,99: comissão de 1%.
* Venda a partir de R$ 500,00: comissão de 5%.

### Executar

```bash
python3 exercicio_1/main.py
```

## Exercício 2 - Movimentação de estoque

O programa permite realizar movimentações de entrada e saída nos produtos cadastrados em `estoque.json`.

Cada movimentação possui:

* identificador único (UUID);
* descrição da movimentação;
* código do produto;
* quantidade final disponível em estoque.

Também são realizadas validações para impedir quantidades inválidas e saídas superiores ao estoque disponível.

O arquivo JSON representa o estoque inicial. As movimentações são realizadas em memória durante a execução e não alteram permanentemente o arquivo original.

### Executar

```bash
python3 exercicio_2/main.py
```

## Exercício 3 - Cálculo de juros

O programa recebe um valor e uma data de vencimento e calcula os juros correspondentes aos dias de atraso até a data atual.

A taxa utilizada é de 2,5% ao dia.

O cálculo adotado utiliza juros simples:

```text
juros = valor × 0,025 × dias de atraso
```

Caso a data de vencimento seja igual ou posterior à data atual, não são aplicados juros.

### Executar

```bash
python3 exercicio_3/main.py
```

## Requisitos

* Python 3.10 ou superior.
* Não são necessárias bibliotecas externas.

## Tecnologias e recursos utilizados

* Python
* JSON
* `pathlib`
* `datetime`
* `uuid`

## Autor

Yan Rosa Ferrari
