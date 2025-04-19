import streamlit as st
import pandas as pd
from datetime import datetime
import sqlite3
import os
import random



def app():
    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
    df = pd.read_csv("crimes.csv",sep=";")
    
    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #

    cpenal = df['art'].tolist()

    civil = ["Casado(a)","Solteiro(a)","Viuvo(a)"]

    with st.form("my_form"):
        # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
        col1,col2,col3,col4,col5 = st.columns(spec=[1,0.50,0.25,0.25,0.50])
        with col1:
            NomeCompleto = st.text_input ("Nome Completo",max_chars = 50)
        with col2:
            Nacionalidade = st.text_input("Nacionalidade",max_chars=20)
        with col3:
            EstadoC = st.selectbox("Estado Civil",civil)
        with col4:
            dataNasc = st.date_input("Data de Nascimento",format= "DD/MM/YYYY",    min_value = datetime(1900, 1, 1), max_value = datetime.today())
        with col5:
            Profissao = st.text_input("Profissão",max_chars=30)


    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
        col6,col7,col8,col9 = st.columns(spec = [.25,.25,.05,.25])
        with col6:
            CPF = st.text_input("CPF",max_chars = 11)
        with col7:
            Endereco = st.text_input("Endereço",max_chars=50)
        with col8:
            Numero = st.text_input("Número",max_chars=4)
        with col9:
            Bairro = st.text_input("Bairro",max_chars=20)
        

    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
        col10,col11,col12,col13,col14 = st.columns(spec=[.50,.50,.10,.25,.25])

        with col10:
            Cidade = st.text_input("Cidade",max_chars=20)
        with col11:
            Estado = st.text_input("Estado",max_chars=20)
        with col12:
            Genero = st.text_input ("gênero",max_chars=1)
        with col13:
            Etnia = st.text_input("Etnia",max_chars=10)
        with col14:
            Acuzacao = st.selectbox("Delito Art.",options = cpenal )

        txt = st.text_area("Resumo",max_chars=500)

    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
        col111,col222,col333 = st.columns(spec=[1,1,1])
        
        with col111:
            pass
        with col222:
            def gerar_id_unico():
                conn = sqlite3.connect('cadastro.db')
                cursor = conn.cursor()
                while True:
                    id_aleatorio = random.randint(0, 99999)  # Gera um número aleatório de 5 dígitos
                    cursor.execute("SELECT id FROM delinquentes WHERE id = ?", (id_aleatorio,))
                    resultado = cursor.fetchone()
                    if not resultado:  # Se o ID não existir no banco, ele é único
                        conn.close()
                        return id_aleatorio
            submitted = st.form_submit_button("Salvar", use_container_width=True, type="secondary")
            if submitted:
                # Captura a data e o horário atual
                data_atual = datetime.now().strftime('%Y-%m-%d')  # Formato de data: YYYY-MM-DD
                hora_atual = datetime.now().strftime('%H:%M:%S')  # Formato de hora: HH:MM:SS

                # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
                # Gera um ID aleatório de 5 dígitos
                id_aleatorio = gerar_id_unico()
                # Conecta ao banco de dados
                conn = sqlite3.connect('cadastro.db')
                cursor = conn.cursor()
            
                cursor.execute('''
            CREATE TABLE IF NOT EXISTS delinquentes (
                id INTEGER PRIMARY KEY,
                Data DATE NOT NULL,
                Hora TIME NOT NULL,
                NomeCompleto TEXT NOT NULL,
                Nacionalidade TEXT NOT NULL,
                EstadoC TEXT NOT NULL,
                DataNasc DATE NOT NULL,       
                Profissao TEXT NOT NULL,
                CPF INT NOT NULL,
                Endereco TEXT NOT NULL,
                Numero INT NOT NULL,
                Bairro TEXT NOT NULL,
                Cidade TEXT NOT NULL,
                Estado TEXT NOT NULL,
                Genero TEXT NOT NULL,
                Etnia TEXT NOT NULL,
                Acuzacao TEXT NOT NULL,
                txt TEXT NOT NULL
                    )
                ''')

                # Insere os dados no banco
cursor.execute('''
INSERT INTO delinquentes (
        id, Data, Hora, NomeCompleto, Nacionalidade, EstadoC, DataNasc, Profissao, CPF, Endereco, Numero, Bairro, Cidade, Estado, Genero, Etnia, Acuzacao, txt
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (
    id_aleatorio, data_atual, hora_atual, NomeCompleto, Nacionalidade, EstadoC, dataNasc, Profissao, CPF, Endereco, Numero, Bairro, Cidade, Estado, Genero, Etnia, Acuzacao, txt
))

                # Obtém o ID da última linha inserida
                

                conn.commit()
                conn.close()

                st.success(f"Dados salvos com sucesso!")
                st.success(f'favor anotar ID para consulta : {id_aleatorio}')
                # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #



                st.write(NomeCompleto)
                st.write(Nacionalidade)
                st.write(EstadoC)
                st.write(dataNasc)
                st.write(Profissao)
                st.write(CPF)
                st.write(Endereco)
                st.write(Numero)
                st.write(Bairro)
                st.write(Cidade)
                st.write(Estado)
                st.write(Genero)
                st.write(Etnia)
                st.write(Acuzacao)
                st.write(txt)
                
        with col333:
            pass
                
