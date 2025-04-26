import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px


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
    dfnew = dfnew.rename(columns={"Acuzacao": "Acusacao"})
    # st.dataframe(dfnew,use_container_width=True,hide_index =True)

    col1, col2 = st.columns([1, 1],vertical_alignment ='center')
    with col1:
        fig = px.pie(dfnew, names="Estado", title="Distribuição por Estado", hole=0.4)
        st.plotly_chart(fig, use_container_width=True)
      
    with col2:
            
        fig = px.bar(dfnew, x="Estado", title="Distribuição por Estado", color="Estado")
        st.plotly_chart(fig, use_container_width=True)
       
        
       
    col3, col4 = st.columns([1, 1],vertical_alignment ='center')
    with col3:
        
        if "DataNasc" in dfnew.columns:
            dfnew["Idade"] = (pd.Timestamp.now() - pd.to_datetime(dfnew["DataNasc"], errors="coerce")).dt.days // 365
            trend = dfnew.groupby("Idade")["Acusacao"].count().reset_index(name="Acusações")
            fig = px.line(trend, x="Idade", y="Acusações", title="Tendência de Acusações por Idade")
            st.plotly_chart(fig, use_container_width=True)
    
    with col4:
       
        fig = px.treemap(dfnew, path=["Estado", "Acusacao"], title="Hierarquia de Acusações por Estado")
        st.plotly_chart(fig, use_container_width=True)


    

    col5, col6 = st.columns([1, 1],vertical_alignment ='center')
    with col5:
        if "DataNasc" in dfnew.columns:
            dfnew["Idade"] = (pd.Timestamp.now() - pd.to_datetime(dfnew["DataNasc"], errors="coerce")).dt.days // 365
            fig = px.scatter(dfnew, x="Idade", y="Acusacao", color="Genero", title="Idade vs Acusação")
            st.plotly_chart(fig, use_container_width=True)

    with col6:
    
        if "DataNasc" in dfnew.columns:
            dfnew["Idade"] = (pd.Timestamp.now() - pd.to_datetime(dfnew["DataNasc"], errors="coerce")).dt.days // 365
            fig = px.histogram(dfnew, x="Idade", nbins=20, title="Distribuição de Idade", color="Genero")
            st.plotly_chart(fig, use_container_width=True)




