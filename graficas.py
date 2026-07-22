import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el Excel generado por el bot
df = pd.read_excel("BotQA-Excel.xlsx")

# --- Gráfico 1: Ofertas por empresa ---
plt.figure(figsize=(8,5))
df['Empresa'].value_counts().plot(kind='bar', color='skyblue')
plt.title("Número de ofertas por empresa")
plt.xlabel("Empresa")
plt.ylabel("Cantidad de ofertas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Gráfico 2: Ofertas por fecha de publicación ---
plt.figure(figsize=(8,5))
df['Fecha'].value_counts().plot(kind='bar', color='orange')
plt.title("Ofertas por fecha de publicación")
plt.xlabel("Fecha")
plt.ylabel("Cantidad de ofertas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Gráfico 3: Ofertas por fuente (URL consultada) ---
plt.figure(figsize=(8,5))
df['Fuente'].value_counts().plot(kind='bar', color='green')
plt.title("Ofertas por fuente")
plt.xlabel("Fuente")
plt.ylabel("Cantidad de ofertas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
