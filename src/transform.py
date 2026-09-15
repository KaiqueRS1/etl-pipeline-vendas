import pandas as pd


STATUS_VALIDOS = {
    "aprovado",
    "cancelado"
}


def transformar_clientes(
    df_clientes: pd.DataFrame
) -> pd.DataFrame:

    df = df_clientes.copy()

    df["nome"] = (
        df["nome"]
        .str.strip()
        .replace("", pd.NA)
    )

    df["email"] = (
        df["email"]
        .str.strip()
        .str.lower()
        .replace("", pd.NA)
    )

    df["cidade"] = (
        df["cidade"]
        .str.strip()
        .replace("", pd.NA)
        .fillna("nao informado")
    )

    return df


def transformar_pedidos(
    df_pedidos: pd.DataFrame
) -> pd.DataFrame:

    df = df_pedidos.copy()

    df["status"] = (
        df["status"]
        .str.strip()
        .str.lower()
        .replace("", pd.NA)
    )

    df = df.drop_duplicates()

    # Mantemos o valor original para investigação
    # caso o registro seja rejeitado.
    df["valor_original"] = (
        df["valor"]
        .astype("string")
    )

    df["valor"] = pd.to_numeric(
        df["valor"],
        errors="coerce"
    )

    df["quantidade"] = pd.to_numeric(
        df["quantidade"],
        errors="coerce"
    )

    df["data_pedido"] = pd.to_datetime(
        df["data_pedido"],
        errors="coerce"
    )

    df["valor_total"] = (
        df["valor"]
        * df["quantidade"]
    )

    return df


def separar_pedidos_validos(
    df_pedidos: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:

    df = df_pedidos.copy()

    df["motivo_rejeicao"] = ""

    condicoes = [
        (
            df["id_pedido"].isna(),
            "id_pedido_ausente"
        ),
        (
            df["id_cliente"].isna(),
            "id_cliente_ausente"
        ),
        (
            ~df["status"].isin(STATUS_VALIDOS),
            "status_invalido"
        ),
        (
            df["valor"].isna(),
            "valor_invalido"
        ),
        (
            df["quantidade"].isna()
            | (df["quantidade"] <= 0),
            "quantidade_invalida"
        ),
        (
            df["data_pedido"].isna(),
            "data_invalida"
        ),
    ]

    for mascara, motivo in condicoes:
        sem_motivo = (
            df["motivo_rejeicao"] == ""
        )

        df.loc[
            mascara & sem_motivo,
            "motivo_rejeicao"
        ] = motivo

    pedidos_rejeitados = df[
        df["motivo_rejeicao"] != ""
    ].copy()

    pedidos_validos = df[
        df["motivo_rejeicao"] == ""
    ].copy()

    pedidos_validos = pedidos_validos.drop(
        columns=[
            "motivo_rejeicao",
            "valor_original"
        ]
    )

    return (
        pedidos_validos,
        pedidos_rejeitados
    )


def consolidar_dados(
    df_clientes: pd.DataFrame,
    df_pedidos: pd.DataFrame
) -> pd.DataFrame:

    df_consolidado = df_pedidos.merge(
        df_clientes,
        on="id_cliente",
        how="left",
        validate="many_to_one"
    )

    return df_consolidado