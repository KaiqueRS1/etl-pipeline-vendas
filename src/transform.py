import pandas as pd


def transformar_clientes(df_clientes: pd.DataFrame) -> pd.DataFrame:
    df = df_clientes.copy()

    df["nome"] = df["nome"].str.strip()

    df["email"] = (
        df["email"]
        .str.strip()
        .str.lower()
    )

    df["cidade"] = (
        df["cidade"]
        .str.strip()
        .fillna("nao informado")
    )
    return df

def transformar_pedidos(df_pedidos: pd.DataFrame) -> pd.DataFrame:
    df = df_pedidos.copy()

    df["status"] = (
        df["status"]
        .str.strip()
        .str.lower()
    )

    df = df.drop_duplicates()

    df["valor"] = pd.to_numeric(
        df["valor"],
        errors="coerce"
    )

    df["data_pedido"] = pd.to_datetime(
        df["data_pedido"]
    )
    return df