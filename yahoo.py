import yfinance as yf
import matplotlib.pyplot as plt

# Descargar datos del índice S&P 500
sp500 = yf.download('^GSPC', start='2020-01-01', end='2025-01-01')

# Mostrar las primeras filas
print(sp500.head())

# Graficar el precio de cierre
plt.figure(figsize=(12, 6))
plt.plot(sp500['Close'], label='S&P 500 Close')
plt.title('S&P 500 Closing Price')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.legend()
plt.grid(True)
plt.show()
