import os
import pandas as pd

class ProcessadorCSV:
    def __init__(self, arquivo_csv):  # Corrigido para __init__
        self.arquivo_csv = arquivo_csv
        self.df = None

    def carregar_csv(self):
        # Verificar se o arquivo CSV existe
        if not os.path.exists(self.arquivo_csv):
            print(f"Erro: O arquivo '{self.arquivo_csv}' não existe.")
            return

        # Carregar arquivo CSV em dataframe
        try:
            self.df = pd.read_csv(self.arquivo_csv)
        except Exception as e:
            print(f"Erro ao ler o arquivo CSV: {e}")

    def remover_celulas_vazias(self):
        # Verificar e remover células vazias
        if self.df is not None:
            self.df = self.df.dropna()

    def filtrar_por_estado(self, estado):
        # Filtrar linhas pela coluna estado
        if self.df is not None:
            if "estado" in self.df.columns:
                self.df = self.df[self.df["estado"] == estado]
            else:
                print("Erro: A coluna 'estado' não existe no DataFrame.")
        else:
            print("Erro: DataFrame não carregado corretamente.")

    def processar(self, estado):
        # Carregar CSV, remover células vazias e filtrar por estado
        self.carregar_csv()
        self.remover_celulas_vazias()
        self.filtrar_por_estado(estado)

        return self.df

# Exemplo:
arquivo_csv = "./exemplo.csv"  # Substitua 'exemplo.csv' pelo caminho do seu arquivo CSV
estado_filtrado = "SP"  # Estado que você quer filtrar

processador = ProcessadorCSV(arquivo_csv)
df_filtrado = processador.processar(estado_filtrado)

if df_filtrado is not None:
    print(df_filtrado)
