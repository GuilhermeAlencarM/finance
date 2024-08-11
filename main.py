import pandas as pd
import streamlit as st
import numpy as np

# Exemplo de dados
formularios = [
    {
        "Data": "07/2024",
        "Operações realizadas": "Ocorreram",
        "Nome da Companhia": "DOMINGOS DA COMPANHIA LWSA S/A",
        "Grupo e Pessoas Ligadas": "Não informado",
        "Saldo Inicial (Quantidade)": 13205972,
        "Movimentações": [
            {
                "Tipo de Título": "Ações",
                "Características dos Títulos": "ON",
                "Nome do intermediário": "BTG",
                "Tipo de operação": "Exercício de subscrição",
                "Dia da operação": 30,
                "Quantidade de títulos negociados": -100000,
                "Preço por título": -1.75000,
                "Volume financeiro da operação (R$)": 332500.00,
            }
        ],
        "Saldo Final (Quantidade)": 13010972
    },
    {
        "Data": "07/2024",
        "Operações realizadas": "Ocorreram",
        "Nome da Companhia": "YAPAY PAGAMENTOS ONLINE LTDA.",
        "Grupo e Pessoas Ligadas": "Controlada",
        "Saldo Inicial (Quantidade)": None,  # Usando None para indicar "Não informado"
        "Movimentações": [
            {
                "Tipo de Título": "Ações",
                "Características dos Títulos": "ON",
                "Nome do intermediário": "BTG",
                "Tipo de operação": "Compra à vista",
                "Dia da operação": 8,
                "Quantidade de títulos negociados": 800000,
                "Preço por título": 4.29554,
                "Volume financeiro da operação (R$)": 3915546.14,
            },
            # Continue com outras movimentações...
            {
                "Tipo de Título": "Ações",
                "Características dos Títulos": "ON",
                "Nome do intermediário": "BTG",
                "Tipo de operação": "Compra à vista",
                "Dia da operação": 10,
                "Quantidade de títulos negociados": 1300000,
                "Preço por título": 4.20660,
                "Volume financeiro da operação (R$)": 5838580.00,
            },
            {
                "Tipo de Título": "Ações",
                "Características dos Títulos": "ON",
                "Nome do intermediário": "BTG",
                "Tipo de operação": "Compra à vista",
                "Dia da operação": 11,
                "Quantidade de títulos negociados": 1300000,
                "Preço por título": 4.64300,
                "Volume financeiro da operação (R$)": 6035770.00,
            },
            {
                "Tipo de Título": "Ações",
                "Características dos Títulos": "ON",
                "Nome do intermediário": "BTG",
                "Tipo de operação": "Compra à vista",
                "Dia da operação": 15,
                "Quantidade de títulos negociados": 930000,
                "Preço por título": 4.29070,
                "Volume financeiro da operação (R$)": 4099665.00,
            },
            {
                "Tipo de Título": "Ações",
                "Características dos Títulos": "ON",
                "Nome do intermediário": "ITAU",
                "Tipo de operação": "Compra à vista",
                "Dia da operação": 17,
                "Quantidade de títulos negociados": 1300000,
                "Preço por título": 4.25200,
                "Volume financeiro da operação (R$)": 5527600.00,
            },
            {
                "Tipo de Título": "Ações",
                "Características dos Títulos": "ON",
                "Nome do intermediário": "ITAU",
                "Tipo de operação": "Compra à vista",
                "Dia da operação": 18,
                "Quantidade de títulos negociados": 1300000,
                "Preço por título": 4.44470,
                "Volume financeiro da operação (R$)": 5775110.00,
            },
            {
                "Tipo de Título": "Ações",
                "Características dos Títulos": "ON",
                "Nome do intermediário": "BTG",
                "Tipo de operação": "Compra à vista",
                "Dia da operação": 22,
                "Quantidade de títulos negociados": 650000,
                "Preço por título": 4.50100,
                "Volume financeiro da operação (R$)": 2925650.00,
            },
            {
                "Tipo de Título": "Ações",
                "Características dos Títulos": "ON",
                "Nome do intermediário": "ITAU",
                "Tipo de operação": "Compra à vista",
                "Dia da operação": 23,
                "Quantidade de títulos negociados": 800000,
                "Preço por título": 4.20032,
                "Volume financeiro da operação (R$)": 3360256.00,
            },
            {
                "Tipo de Título": "Ações",
                "Características dos Títulos": "ON",
                "Nome do intermediário": "ITAU",
                "Tipo de operação": "Compra à vista",
                "Dia da operação": 24,
                "Quantidade de títulos negociados": 650000,
                "Preço por título": 4.31250,
                "Volume financeiro da operação (R$)": 2873975.00,
            },
            {
                "Tipo de Título": "Ações",
                "Características dos Títulos": "ON",
                "Nome do intermediário": "BTG",
                "Tipo de operação": "Compra à vista",
                "Dia da operação": 24,
                "Quantidade de títulos negociados": 1300000,
                "Preço por título": 4.43590,
                "Volume financeiro da operação (R$)": 5761831.50,
            },
        ],
        "Saldo Final (Quantidade)": 13020800
    }
]

# Função para converter movimentações em DataFrame
def movimentacoes_to_df(formulario):
    return pd.DataFrame(formulario["Movimentações"])

# Função para criar o DataFrame principal
def criar_dataframe(formularios):
    rows = []
    for formulario in formularios:
        for mov in formulario["Movimentações"]:
            row = {
                "Data": formulario["Data"],
                "Operações realizadas": formulario["Operações realizadas"],
                "Nome da Companhia": formulario["Nome da Companhia"],
                "Grupo e Pessoas Ligadas": formulario["Grupo e Pessoas Ligadas"],
                "Saldo Inicial (Quantidade)": formulario["Saldo Inicial (Quantidade)"],
                "Saldo Final (Quantidade)": formulario["Saldo Final (Quantidade)"],
                **mov
            }
            rows.append(row)
    df = pd.DataFrame(rows)

    # Substituir "None" ou "NaN" nas colunas numéricas
    df["Saldo Inicial (Quantidade)"] = pd.to_numeric(df["Saldo Inicial (Quantidade)"], errors='coerce')
    df["Saldo Final (Quantidade)"] = pd.to_numeric(df["Saldo Final (Quantidade)"], errors='coerce')

    return df

# Criar DataFrame
df = criar_dataframe(formularios)

# Adicionar título no Streamlit
st.title("Relatório de Movimentações de Valores Mobiliários")

# Exibir DataFrame no Streamlit
st.write("Movimentações de Valores Mobiliários")
st.dataframe(df)

# Adicionar botão para exportar DataFrame como CSV
st.write("\n")
if st.button("Exportar para CSV"):
    csv = df.to_csv(index=False)
    st.download_button(
        label="Baixar CSV",
        data=csv,
        file_name='movimentacoes_valores_mobiliarios.csv',
        mime='text/csv',
    )
