import logging

from src.config import (
    CLIENTES_RAW,
    PEDIDOS_RAW,
    VENDAS_PROCESSADAS_CSV,
    VENDAS_PROCESSADAS_PARQUET,
    PEDIDOS_REJEITADOS_CSV,
)

from src.extract import extrair_csv

from src.transform import (
    transformar_clientes,
    transformar_pedidos,
    separar_pedidos_validos,
    consolidar_dados,
)

from src.validate import (
    validar_clientes,
    validar_pedidos,
    validar_consolidado,
)

from src.load import (
    carregar_csv,
    carregar_parquet,
)


logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(message)s"
    )
)

logger = logging.getLogger(__name__)


def main() -> None:

    try:
        logger.info(
            "Pipeline iniciado"
        )

        # EXTRACT
        df_clientes = extrair_csv(
            CLIENTES_RAW
        )

        df_pedidos = extrair_csv(
            PEDIDOS_RAW
        )

        logger.info(
            "Extração concluída: "
            "%s clientes e %s pedidos",
            len(df_clientes),
            len(df_pedidos),
        )

        # TRANSFORM
        df_clientes = transformar_clientes(
            df_clientes
        )

        df_pedidos = transformar_pedidos(
            df_pedidos
        )

        (
            df_pedidos,
            df_rejeitados
        ) = separar_pedidos_validos(
            df_pedidos
        )

        logger.info(
            "Transformação concluída: "
            "%s pedidos válidos e "
            "%s rejeitados",
            len(df_pedidos),
            len(df_rejeitados),
        )

        # VALIDATE
        validar_clientes(
            df_clientes
        )

        validar_pedidos(
            df_pedidos
        )

        # CONSOLIDAÇÃO
        df_consolidado = consolidar_dados(
            df_clientes,
            df_pedidos
        )

        validar_consolidado(
            df_consolidado
        )

        # LOAD
        carregar_csv(
            df_consolidado,
            VENDAS_PROCESSADAS_CSV
        )

        carregar_parquet(
            df_consolidado,
            VENDAS_PROCESSADAS_PARQUET
        )

        carregar_csv(
            df_rejeitados,
            PEDIDOS_REJEITADOS_CSV
        )

        logger.info(
            "Carga concluída"
        )

        logger.info(
            "Pipeline finalizado com sucesso"
        )

    except Exception:
        logger.exception(
            "Pipeline finalizado com erro"
        )
        raise


if __name__ == "__main__":
    main()