import pandas as pd


def extrair_csv(caminho_arquivo: str) -> pd.DataFrame:
    df = pd.read_csv(caminho_arquivo)

    return df