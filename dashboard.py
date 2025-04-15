import streamlit as st
import pandas as pd
import sqlite3
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report 

def app():
    # st.title("Dashboard ")

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
    # st.subheader("Tabela de Delinquentes")

    dfnew = df[["NomeCompleto","Nacionalidade","EstadoC","DataNasc","Profissao","CPF",
    "Endereco","Numero","Bairro","Cidade","Estado","Genero","Etnia","Acuzacao","txt"]]
    st.dataframe(dfnew,use_container_width=True,hide_index =True)
    
    # Exibe métricas
    # st.subheader("Métricas")
    # total_delinquentes = len(df)

    # nacionalidades = df["nacionalidade"].nunique() if "nacionalidade" in df.columns else 0
    # acusacoes = df["acusacao"].nunique() if "acusacao" in df.columns else 0

    col1, col2, col3 = st.columns([1, .11, 1],vertical_alignment ='center',border=True)
    with col1:
        pass
        # st.metric("Total ", total_delinquentes)
    with col2:
        acusados = dfnew["Acuzacao"].unique()
        st.metric("Delitos", len(acusados)) 
        
        # st.metric("Nacionalidades Únicas", nacionalidades)
    with col3:
        pass
        # st.metric("Tipos de Acusação", acusacoes)


    # st.scatter_chart(df, x="Data", y="Acuzacao", use_container_width=True,x_label= "Tempo",y_label = "Artigos",color = "Acuzacao",size ="Acuzacao")
    profile = ProfileReport(dfnew, title="Relatório de Perfil dos Dados", explorative=True)
    st_profile_report(profile)