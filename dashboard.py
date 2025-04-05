import streamlit as st
import pandas as pd
import sqlite3

def app():
    df = pd.read_csv("crimes.csv", sep=";")

    col900, col901, col902 = st.columns(spec=[1, .75, 1])
    with col900:
        pass
    with col901:
        idRandom = st.text_input("Informe ID", max_chars=4)
    with col902:
        pass

    if st.button("Buscar", type="primary", use_container_width=True):
        # Reseta o session_state antes de realizar uma nova busca
        st.session_state.resultado = None

        # Conecta ao banco de dados
        try:
            conn = sqlite3.connect("cadastro.db")
            cursor = conn.cursor()

            # Consulta o banco de dados para verificar se o ID existe
            cursor.execute("SELECT * FROM delinquentes WHERE id = ?", (idRandom,))
            st.session_state.resultado = cursor.fetchone()  # Salva o resultado no estado
            conn.close()
        except sqlite3.Error as e:
            st.error(f"Erro ao acessar o banco de dados: {e}")
            return
    if st.session_state.resultado:
        resultado = st.session_state.resultado
        st.success("Registro encontrado:")
    
    if resultado:
        for index, row in df.iterrows():
            try:
                if str(resultado[16]) in df["art"].astype(str).values:
                    st.write(f"Artigo encontrado: {row['art']}")
                    if pd.notna(row["anoMax"]) and pd.notna(row["anoMin"]):
                        st.write(f"Artigo encontrado: {row['anoMax']} e {row['anoMin']}")
                        resultAno = (row["anoMax"] - row["anoMin"]) * 360
                        resultAno = resultAno * 2 / 8
                        resultAno = resultAno / 360

                        st.write(f"Resultado: {resultAno}")

                        result_strAno = str(resultAno)
                        split_result = result_strAno.split(".")
                        if len(split_result) > 0 and int(split_result[0]) != 0:
                            st.write(f"Resultado: {split_result[0]} ano(s)")
                        if len(split_result) > 1 and split_result[1] != '0':
                            decimal_part = int(split_result[1])
                            final_result = round((decimal_part / 100) * 12, 2)
                            final_result = round(final_result * 10, 2)
                            final_result = int(final_result)
                            st.write(f"Sentenciado a : {split_result[0]} ano(s) e {final_result} mês(es)")
                        break
            except KeyError as e:
                st.error(f"Erro: A coluna {e} não foi encontrada no DataFrame.")
                break

    mew = st.button("calcular")
    if mew and 'resultAno' in locals():
        st.header(f"O resultado é: {resultAno}")
    else:
        st.header("Nenhum resultado encontrado")