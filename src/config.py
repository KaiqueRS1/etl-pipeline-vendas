from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
REJECTED_DIR = DATA_DIR / "rejected"

CLIENTES_RAW = RAW_DIR / "clientes.csv"
PEDIDOS_RAW = RAW_DIR / "pedidos.csv"

VENDAS_PROCESSADAS_CSV = (
    PROCESSED_DIR / "vendas_processadas.csv"
)

VENDAS_PROCESSADAS_PARQUET = (
    PROCESSED_DIR / "vendas_processadas.parquet"
)

PEDIDOS_REJEITADOS_CSV = (
    REJECTED_DIR / "pedidos_rejeitados.csv"
)