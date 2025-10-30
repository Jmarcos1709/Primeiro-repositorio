#hboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Meu primeiro dashboard")
st.subheader("Análise de Dados com Streamlit")
st.write("Este é um exemplo simples de dashboard usando Streamlit.")
# Carregar dados
file = "empresas_desempenho.csv"
df = pd.read_csv(file)
#Grafico de barras
df_grouped = df.groupby("Setor")["Receita"].sum().reset_index()
fig = plt.figure(figsize=(8,5))
plt.title("Grafico de barras setor x Receita")
plt.xlabel("Setor")
plt.ylabel("Receita")

st.pyplot(fig)