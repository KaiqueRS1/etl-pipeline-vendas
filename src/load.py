from pathlib import Path

import pandas as pd


def carregar_csv(
    df: pd.DataFrame,
    caminho_arquivo: str | Path
) -> None:

    caminho = Path(caminho_arquivo)

    caminho.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        caminho,
        index=False
    )


def carregar_parquet(
    df: pd.DataFrame,
    caminho_arquivo: str | Path
) -> None:

    caminho = Path(caminho_arquivo)

    caminho.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_parquet(
        caminho,
        index=False
    )