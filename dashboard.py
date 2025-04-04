import streamlit as st
import pandas as pd
import sqlite3

def app():
    df = pd.read_csv("crimes.csv",sep=";")

    
    col900,col901,col902 = st.columns(spec=[1,.75,1])
    with col900:
        pass
    with col901:
        idRandom = st.text_input("Informe ID",max_chars=4)
    with col902:
        pass
    if st.button("Buscar", type="primary", use_container_width=True):
    # Conecta ao banco de dados
        conn = sqlite3.connect('cadastro.db')
        cursor = conn.cursor()

        # Consulta o banco de dados para verificar se o ID existe
        cursor.execute("SELECT * FROM delinquentes WHERE id = ?", (idRandom,))
        resultado = cursor.fetchone()

        conn.close()
        if "resultado" not in st.session_state:
            st.session_state.resultado = None
        # Verifica se o ID foi encontrado
        if resultado:
            # Exibe os dados do registro encontrado
            st.success("Registro encontrado:")

    
        for index, row in df.iterrows():
            try:
                if str(resultado[16]) in df["art"].astype(str).values:
                    st.write(f"Artigo encontrado: {row['art']}")
                    
                    
                    if pd.notna(row["anoMax"]) and pd.notna(row["anoMin"]):
                        st.write(f"Artigo encontrado: {row['anoMax']} e {row['anoMin']}")
                        
                        result = (row["anoMax"] - row["anoMin"]) * 360
                        result = result * 2/8

                        result = result / 360
                        st.write(f"Resultado: {result}")
                        result_str = str(result)
                        split_result = result_str.split(".")
                        if len(split_result) > 0 and int(split_result[0]) != 0:
                            st.write(f"Resultado: {split_result[0]} ano(s)")

                        breakpoint()
            except KeyError as e:
                print(f"Erro: A coluna {e} não foi encontrada no DataFrame.")
                break
            
        mew = st.button("calcular")
        if mew:
            st.header(f"O resultado é: {result}")
        else:
            st.header("Nenhum resultado encontrado")
    