# %% [markdown]
# <a href="https://colab.research.google.com/github/ferranfont/Introduccion_al_trading_algoritmico/blob/main/API_IEX.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %%
import pandas as pd
import numpy as np
import requests
import matplotlib
import math


# %%
drive.mount('/content/drive')

# %%
acciones = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/sp_500_stocks.csv')


# %%
  seleccion = acciones['Ticker'].loc[344]
  seleccion

# %%
acciones.head(20)

# %%
diccionario = {'eurusd':1.2344,'gbpusd':0.8854,'audusd':1.4532}
diccionario

# %%
diccionario['gbpusd']

# %%
symbol='MSC'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token=Tpk_059b97af715d417d9f49f50b51b1c448'
data = requests.get(api_url).json()
data


# %%
ultimo_precio = data['latestPrice']
ultimo_precio

# %%
ultimo_cierre = data['previousClose']
ultimo_cierre

# %%
for i in range(0,502):
  seleccion = acciones['Ticker'].loc[i]
  print(seleccion)


# %%
def subida(a,b):
  diferencial = ((b-a)/a)*100
  # redondeo_diferencial = round(diferencial,2)
  print ('La subida ha sido del:',round(diferencial,2),'%')

# %%
subida(ultimo_cierre,ultimo_precio)

# %%
for i in range (0,14):
  symbol = acciones['Ticker'].loc[i]
  #print(symbol)
  api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token=Tpk_059b97af715d417d9f49f50b51b1c448'
  data = requests.get(api_url).json()
  ultimo_precio = data['latestPrice']
  description = data['companyName']
  print('El último precio de:', symbol,'-', description, ' ha sido: ', ultimo_precio,'$\n')

# %%

for i in data:
  
  print(i)

# %%

seleccion = acciones['Ticker'].loc[4]
print(seleccion)

# %%
  symbol = acciones['Ticker'].loc[36]
  print(symbol)

# %% [markdown]
# Append alternativo en dataframe

# %%
# Creamos un DataFrame vacío el cuál lo rellenamos con filas nuevas con el método append. Finalmente filtramos las columnas que nos interesan.
final_dataframe = pd.DataFrame() 

for i in range (15):
  symbol = acciones['Ticker'].loc[i]
  api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token=Tpk_059b97af715d417d9f49f50b51b1c448'
  data = requests.get(api_url).json()
  final_dataframe = final_dataframe.append([data])

final_dataframe[['symbol','companyName','iexClose']]



