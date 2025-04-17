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
    
    dfnew = df[["NomeCompleto","Nacionalidade","EstadoC","DataNasc","Profissao","CPF",
    "Endereco","Numero","Bairro","Cidade","Estado","Genero","Etnia","Acuzacao","txt"]]
    st.dataframe(dfnew,use_container_width=True,hide_index =True)

    col1, col2, col3 = st.columns([1, .11, 1],vertical_alignment ='center')
    with col1:
        pass
      
    with col2:
        pass
        
       
    with col3:
        pass
       


    # st.scatter_chart(df, x="Data", y="Acuzacao", use_container_width=True,x_label= "Tempo",y_label = "Artigos",color = "Acuzacao",size ="Acuzacao")
    # profile = ProfileReport(dfnew, title="Relatório de Perfil dos Dados", explorative=True)
    # st_profile_report(profile)


    pikachu_df = pd.read_csv("localizacao.csv")

    # Remove linhas com valores nulos nas colunas latitude e longitude
    pikachu_df = pikachu_df.dropna(subset=["latitude", "longitude"])

    # Certifique-se de que latitude e longitude são do tipo numérico
    pikachu_df["latitude"] = pd.to_numeric(pikachu_df["latitude"], errors="coerce")
    pikachu_df["longitude"] = pd.to_numeric(pikachu_df["longitude"], errors="coerce")

    # Exibe o mapa
    st.map(pikachu_df, zoom=4, use_container_width=True)