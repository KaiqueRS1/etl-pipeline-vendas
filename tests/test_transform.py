import pandas as pd

from src.transform import (
    transformar_clientes,
    transformar_pedidos,
    separar_pedidos_validos,
)


def test_transformar_clientes():

    entrada = pd.DataFrame([
        {
            "id_cliente": 1,
            "nome": " Ana ",
            "email": " ANA@EMAIL.COM ",
            "cidade": None,
        }
    ])

    resultado = transformar_clientes(
        entrada
    )

    assert resultado.loc[0, "nome"] == "Ana"

    assert (
        resultado.loc[0, "email"]
        == "ana@email.com"
    )

    assert (
        resultado.loc[0, "cidade"]
        == "nao informado"
    )


def test_separar_pedido_invalido():

    entrada = pd.DataFrame([
        {
            "id_pedido": 1,
            "id_cliente": 1,
            "data_pedido": "2026-08-01",
            "status": "APROVADO",
            "valor": "erro",
            "quantidade": 2,
        }
    ])

    transformado = transformar_pedidos(
        entrada
    )

    validos, rejeitados = (
        separar_pedidos_validos(
            transformado
        )
    )

    assert len(validos) == 0
    assert len(rejeitados) == 1

    assert (
        rejeitados.iloc[0]["motivo_rejeicao"]
        == "valor_invalido"
    )