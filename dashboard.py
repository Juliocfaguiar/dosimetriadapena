import streamlit as st
import pandas as pd
import sqlite3

def app():
    st.title("Dashboard - Delinquentes")

    # Conexão com o banco de dados
    try:
        conn = sqlite3.connect("cadastro.db")
        query = "SELECT * FROM delinquentes"
        df = pd.read_sql_query(query, conn)
        conn.close()
    except sqlite3.Error as e:
        st.error(f"Erro ao acessar o banco de dados: {e}")
        return

    # Exibe os dados em uma tabela
    st.subheader("Tabela de Delinquentes")
    st.dataframe(df)

    # Exibe métricas
    st.subheader("Métricas")
    total_delinquentes = len(df)
    nacionalidades = df["nacionalidade"].nunique() if "nacionalidade" in df.columns else 0
    acusacoes = df["acusacao"].nunique() if "acusacao" in df.columns else 0

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Delinquentes", total_delinquentes)
    with col2:
        st.metric("Nacionalidades Únicas", nacionalidades)
    with col3:
        st.metric("Tipos de Acusação", acusacoes)
