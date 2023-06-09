# -*- coding: utf-8 -*-
"""Python - Aula03_CSV.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cYWeB0Y5tG3Z1zR7bHUkli9noDIYRwWh

###01 - **Base** de Dados no GoogleDrive

* Primeiro, precisa rodar o código abaixo. Aparecerá um link, basta clicar que irá abrir uma outra página. Selecione a conta do gmail. Aparecerá um código. Basta copiar o código e colar no campo que apareceu neste notebook.
"""

from google.colab import drive
drive.mount('/content/drive')

"""#1.1) *Caminho da base de dados*
* Depois, selecione o ícone da pasta no menu lateral esquerdo do notebook. Existirá uma pasta chamada drive, com os arquivos do seu drive.*texto em itálico* Encontre o caminho **do** csv e adicione na variável path abaixo.
"""

path = '/content/drive/MyDrive/MovimentoFinanceiroCSV.csv'

"""#1.2) Lendo a base de dados
* Leia o csv com o pandas. Precisa mudar o separador (parâmetro sep) e o encoding.
"""

import pandas as pd
path = '/content/drive/MyDrive/MovimentoFinanceiroCSV.csv'
df = pd.read_csv(path, sep=';', encoding = "ISO-8859-1")
df

"""* Para alterar e fazer com que os nomes da coluna apareçam na linha 1 (Data, Amostra ...), use as linhas de código a seguir:"""

names = df.iloc[1, :].values
df = df.iloc[2:, :]
df.columns = names
df

names

"""#1.3) Metodos **HEAD** e **TAIL**"""

df.head(3)

df.tail(5)

"""#1.4) Métodos **DESCRIBE** e **INFO**
describe () é usado para gerar estatísticas descritivas dos dados em um DataFrame ou Série do Pandas. Ele resume a tendência central e a dispersão do conjunto de dados. describe () ajuda a obter uma visão geral rápida do conjunto de dados.

O método INFO também serve para obter informações sobre o dataframe 
"""

df.describe()

df.info()

"""#1.5) Método **memory_usage()**
memory_usage () retorna uma série Pandas com o uso de memória de cada coluna (em bytes) em um DataFrame Pandas. Ao especificar o atributo deep como True, podemos saber o espaço real que está sendo ocupado por cada coluna. Mais detalhes sobre memory_usage () podem ser encontrados aqui.

O uso de memória de cada coluna foi fornecido como saída em uma série Pandas. É importante saber o uso de memória de um DataFrame, para que você possa resolver erros como MemoryError em Python.
"""

df.memory_usage(deep=True)

"""#1.6) Método **loc[:]**
Ajuda a acessar um grupo de linhas e colunas em um conjunto de dados, uma fatia do conjunto de dados, conforme nossa necessidade. Por exemplo, se quisermos apenas as 2 últimas linhas e as 3 primeiras colunas de um conjunto de dados, podemos acessá-los com a ajuda de loc [:]. Também podemos acessar linhas e colunas com base em rótulos em vez de número de linha e coluna.
"""

df.loc[29:31, ['Data', 'Projeto', 'Categoria']]

"""#1.7) Método **value_counts**
value_counts () retorna uma série Pandas contendo as contagens de valores únicos. Considere um conjunto de dados que contém informações de clientes sobre 5.000 clientes de uma empresa. value_counts () nos ajudará a identificar o número de ocorrências de cada valor único em uma série. Ele pode ser aplicado a colunas contendo dados como Estado, Indústria de emprego ou idade dos clientes.
"""

contagemEntradasSaidas = df['E/S'].value_counts()
contagemEntradasSaidas

contagemProjetos = df['Projeto'].value_counts()
contagemProjetos

contagemEstados = df['Estado'].value_counts()
contagemEstados

"""#1.8) **Método .Keys()** para obter rótulo dos gráficos

A partir do arquivo ***categoricalVariables.ipynb*** aprendemos como criar gráficos para variáveis categóricas
Mais especificamente, aprendemos a utilizar o **método .keys() **de um dataframe e criar uma lista de nomes que serão utilizados nos rótulos dos gráficos

O **método keys()** retorna um objeto Index com os nomes das colunas. O objeto Index é como uma lista, com os nomes das colunas como itens da lista.
"""

import matplotlib.pyplot as plt

namesEstados = list(contagemEstados.keys())
namesEstados[0] = 'RJ'
namesEstados[1] = 'MG'
namesEstados[2] = 'SP'
namesEstados[3] = 'SC'

fig, axs = plt.subplots(1, 4, figsize=(9, 3), sharey=True)
axs[0].bar(namesEstados, contagemEstados)
axs[1].scatter(namesEstados, contagemEstados)
axs[2].plot(namesEstados, contagemEstados)
fig.suptitle('Categorical Plotting')

contagemEstados.values[0]

contagemEstados['quantidade'] = df['Estado'].value_counts()

df.loc[:, 'Estado'].hist()



import pandas as pd
import plotly.express as px

path = '/content/drive/MyDrive/MovimentoFinanceiroCSV.csv'
df = pd.read_csv(path, sep=';', encoding = "ISO-8859-1")

df

names = df.iloc[1, :].values
df = df.iloc[2:, :]
df.columns = names

fig1 = px.line(df, x = 'Projeto', y = ' Valor ', title='Gráfico de linha')
fig1.show()

fig2 = px.bar(df, x = 'Projeto', y = ' Valor ', title='Gráfico de Barras')
fig2.show()

fig3 = px.scatter(df, x = 'Projeto', y = ' Valor ', title='Gráfico de Barras')
fig3.show()

import matplotlib.pyplot
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [105235, 107697, 110256, 109236, 108859, 109986]

matplotlib.pyplot.plot(meses, valores)
matplotlib.pyplot.show()

"""#1.9) Método **ylim()**
os valores no nosso eixo Y são muito próximos um dos outros. Por isso, qualquer mudança nos valores para mais, ou para menos, podem causar distorções no gráfico.
Para evitar um pouco esse comportamento, podemos mudar os valores da base e do topo do eixo Y, ou seja, podemos alterar seu limite 
usando o método 

"""

matplotlib.pyplot.plot(meses, valores)
matplotlib.pyplot.ylim(100000, 120000)
matplotlib.pyplot.show()

"""#1.10) TÍTULO NO GRÁFICO E NOS EIXOS
## Para detalhar as informações no gráfico
"""

matplotlib.pyplot.title('Faturamento no primeiro semestre de 2017')
matplotlib.pyplot.xlabel('Meses')
matplotlib.pyplot.ylabel('Faturamento em R$')
matplotlib.pyplot.plot(meses, valores)
matplotlib.pyplot.ylim(100000, 120000)
matplotlib.pyplot.show()

import numpy as np
from matplotlib import pyplot as plt

y = 200 + np.random.randn(100)
x = [x for x in range(len(y))]

plt.plot(x, y, '-')
plt.fill_between(x, y, 195, where=(y > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

"""#02 - **Referências Bibliográficas**
#https://plotly.com/python/plot-data-from-csv/
#https://www.w3schools.com/python/pandas/ref_df_keys.asp
#https://www.w3schools.com/python/pandas/pandas_cleaning.asp


"""

