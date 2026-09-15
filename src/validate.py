import pandas as pd


STATUS_VALIDOS = {
    "aprovado",
    "cancelado"
}


def validar_colunas(
    df: pd.DataFrame,
    colunas_obrigatorias: set[str],
    nome_dataset: str
) -> None:

    colunas_ausentes = (
        colunas_obrigatorias
        - set(df.columns)
    )

    if colunas_ausentes:
        raise ValueError(
            f"{nome_dataset}: colunas ausentes: "
            f"{colunas_ausentes}"
        )


def validar_clientes(
    df_clientes: pd.DataFrame
) -> None:

    colunas = {
        "id_cliente",
        "nome",
        "email",
        "cidade"
    }

    validar_colunas(
        df_clientes,
        colunas,
        "clientes"
    )

    if df_clientes.empty:
        raise ValueError(
            "Dataset de clientes está vazio"
        )

    if df_clientes["id_cliente"].isna().any():
        raise ValueError(
            "Existem clientes sem id_cliente"
        )

    if df_clientes["id_cliente"].duplicated().any():
        raise ValueError(
            "Existem id_cliente duplicados"
        )

    if df_clientes["nome"].isna().any():
        raise ValueError(
            "Existem clientes sem nome"
        )

    if df_clientes["email"].isna().any():
        raise ValueError(
            "Existem clientes sem email"
        )

    if df_clientes["cidade"].isna().any():
        raise ValueError(
            "Existem clientes sem cidade"
        )


def validar_pedidos(
    df_pedidos: pd.DataFrame
) -> None:

    colunas = {
        "id_pedido",
        "id_cliente",
        "data_pedido",
        "status",
        "valor",
        "quantidade",
        "valor_total"
    }

    validar_colunas(
        df_pedidos,
        colunas,
        "pedidos"
    )

    if df_pedidos.empty:
        raise ValueError(
            "Não existem pedidos válidos"
        )

    if df_pedidos["id_pedido"].isna().any():
        raise ValueError(
            "Existem pedidos sem id_pedido"
        )

    if df_pedidos["id_pedido"].duplicated().any():
        raise ValueError(
            "Existem id_pedido duplicados"
        )

    if df_pedidos["id_cliente"].isna().any():
        raise ValueError(
            "Existem pedidos sem id_cliente"
        )

    if df_pedidos["valor"].isna().any():
        raise ValueError(
            "Existem valores inválidos"
        )

    if (df_pedidos["valor"] <= 0).any():
        raise ValueError(
            "Existem valores menores ou iguais a zero"
        )

    if (
        df_pedidos["quantidade"].isna().any()
    ):
        raise ValueError(
            "Existem quantidades nulas"
        )

    if (
        df_pedidos["quantidade"] <= 0
    ).any():
        raise ValueError(
            "Existem quantidades inválidas"
        )

    if (
        df_pedidos["data_pedido"]
        .isna()
        .any()
    ):
        raise ValueError(
            "Existem datas inválidas"
        )

    if not (
        df_pedidos["status"]
        .isin(STATUS_VALIDOS)
        .all()
    ):
        raise ValueError(
            "Existem status inválidos"
        )


def validar_consolidado(
    df_consolidado: pd.DataFrame
) -> None:

    if df_consolidado.empty:
        raise ValueError(
            "Dataset consolidado está vazio"
        )

    if df_consolidado["nome"].isna().any():
        raise ValueError(
            "Existem pedidos associados "
            "a clientes inexistentes"
        )