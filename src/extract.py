from pathlib import Path

import pandas as pd


def extrair_csv(
    caminho_arquivo: str | Path
) -> pd.DataFrame:

    caminho = Path(caminho_arquivo)

    if not caminho.exists():
        raise FileNotFoundError(
            f"Arquivo não encontrado: {caminho}"
        )

    df = pd.read_csv(caminho)

    return df