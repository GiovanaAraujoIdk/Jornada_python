#titulo - Sistema de Vendas
#Seção - Cadastrar vendas
    #Campo DATA
    #Campo Vendedor - Ana, bruno, Carla
    #Campo Produto - Notebook, Celular, Tablet
    #Campo Quantidade
    #Campo Valor
    #Botão Cadastrar Vendas
    #quanto eu clicar no botão cadastrar vendas -> adicionar a venda na tabela
#Seção Vendas Cadastradas
    #tabela com as vendas
#Seção Dashboard
    #Card/Metrica -> Faturamento Total
    #Grafico de Barra/Coluna -> Vendas por vendedor
    #Grafico de Pizza -> Vendas por produto
    #streamlit, pandas, plotly
    #streamlit run codigo.py
import streamlit as st
import pandas as pd
import plotly.express as px

#carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")
st.write("# Sistema de Vendas")

#seção de cadastro de vendas

st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Vendas")

#Logica de cadastro

if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    print(nova_venda)
    ultima_linha = len(tabela_vendas) #124 linhas
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda Cadastrada com Sucesso!")
#seção de visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)


#seção de dashboard
st.write("## Dashboard")

#Card/Metrica -> Faturamento Total
faturamento = tabela_vendas['valor'].sum()
st.metric("Faturamento Total", f"R$ {faturamento:,.2f}")
#Grafico de Barra/Coluna -> Vendas por vendedor
grafico1 = px.bar(tabela_vendas, x='vendedor', y='valor', color="produto", color_discrete_map={"Notebook": "pink", "Celular": "blue", "Fone": "purple"})
st.plotly_chart(grafico1)
#Grafico de Pizza -> Vendas por produto
grafico2 = px.pie(tabela_vendas, names='produto', values='valor', hole = 0.5)
st.plotly_chart(grafico2)