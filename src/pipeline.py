from src.extract import extrair_csv
from src.transform import transformar_clientes
from src.transform import transformar_pedidos

def main():
    df_clientes = extrair_csv("data/raw/clientes.csv")
    df_pedidos = extrair_csv("data/raw/pedidos.csv")

    df_clientes = transformar_clientes(df_clientes)
    df_pedidos = transformar_pedidos(df_pedidos)

    print("====== CLIENTES TRATADOS ======")
    print(df_clientes)

    print("\n====== PEDIDOS TRATADOS ======")
    print(df_clientes)
if __name__ == "__main__":
    main()