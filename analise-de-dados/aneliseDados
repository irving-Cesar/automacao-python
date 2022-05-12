# !pip install plotly

import pandas as pd
import plotly.express as px

# Base de Dados: https://drive.google.com/drive/folders/1T7D0BlWkNuy_MDpUHuBG44kT80EmRYIs?usp=sharing

# receber dados
tabela = pd.read_csv('telecom_users.csv')

# axis = 1 -> Coluna, axis = 0 -> Linha
# Exluindo tabela
tabela = tabela.drop('Unnamed: 0', axis=1)

# ajustar type dos valores. Passando valores Text -> numeric
# erros='coerce' -> passar valor NaN à linha caso o valor não for válido 
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# deletar colunas que estão com valores nulos
tabela = tabela.dropna(how='all', axis=1)

# analisar e apagar linhas que estão com alguns valores nulos
tabela = tabela.dropna(how='any', axis=0)

print(tabela['Churn'].value_counts()) # contando quantos 'sim' e 'não' tem na tabela
print(tabela['Churn'].value_counts(normalize=True).map('{:.1%}'.format)) # Porcentagem

# criar gráfico
for coluna in tabela.columns:
    print('\nGráfico da tabela {} x Churn: '.format(coluna))
    
    # criando gráficos e comparando as colunas
    grafic = px.histogram(tabela, x=coluna, color='Churn')

    # mostrar gráfico
    grafic.show()


# informação da tabela
# print(tabela.info())

# mostrar tabela
# display(tabela)
