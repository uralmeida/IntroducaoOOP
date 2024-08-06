import pandas as pd

def processar_dados_vendas(arquivo_csv: str, estado: str) -> pd.DataFrame:
    """
    Processa dados de vendas a partir de um arquivo CSV, removendo dados ausentes,
    filtrando por estado e calculando métricas de vendas.

    Args:
        arquivo_csv (str): O caminho do arquivo CSV com dados de vendas.
        estado (str): O estado pelo qual as linhas serão filtradas.

    Returns:
        pd.DataFrame: DataFrame com as vendas totais e médias por mês.
    """
    try:
        df = pd.read_csv(arquivo_csv)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_csv}' não foi encontrado.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return pd.DataFrame()

    # Preenchimento de valores ausentes
    df.fillna({'vendas': 0}, inplace=True)

    # Verificação da coluna 'estado'
    if 'estado' not in df.columns:
        print("Erro: A coluna 'estado' não existe no DataFrame.")
        return pd.DataFrame()

    # Filtragem por estado
    df_estado = df[df['estado'] == estado]

    # Conversão da coluna de data e extração do mês
    df_estado['data'] = pd.to_datetime(df_estado['data'], errors='coerce')
    df_estado['mes'] = df_estado['data'].dt.month

    # Agrupamento e cálculo de métricas
    vendas_resumo = df_estado.groupby('mes').agg(total_vendas=('vendas', 'sum'), media_vendas=('vendas', 'mean')).reset_index()

    # Exibir o resumo
    print("Resumo das vendas por mês:")
    print(vendas_resumo)

    return vendas_resumo

# Exemplo de uso
arquivo_csv = "./dados_vendas.csv"
estado_filtrado = "SP"
df_resumo = processar_dados_vendas(arquivo_csv, estado_filtrado)

print(df_resumo)
