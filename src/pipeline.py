from src.extract import extrair_csv


def main():
    df_clientes = extrair_csv("data/raw/clientes.csv")
    df_pedidos = extrair_csv("data/raw/pedidos.csv")

    print("====== CLIENTES ======")
    print(df_clientes)

    print("\n====== PEDIDOS ======")
    print(df_pedidos)


if __name__ == "__main__":
    main()