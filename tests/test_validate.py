import pandas as pd
import pytest

from src.validate import validar_clientes


def test_cliente_valido():

    df = pd.DataFrame([
        {
            "id_cliente": 1,
            "nome": "Ana",
            "email": "ana@email.com",
            "cidade": "Barra Mansa",
        }
    ])

    validar_clientes(df)


def test_cliente_sem_email():

    df = pd.DataFrame([
        {
            "id_cliente": 1,
            "nome": "Ana",
            "email": None,
            "cidade": "Barra Mansa",
        }
    ])

    with pytest.raises(ValueError):
        validar_clientes(df)