import streamlit as st
import pandas as pd
import sqlite3

def app():
    df = pd.read_csv("crimes.csv",sep=";")


    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
    
    col200, col201,col202 = st.columns([1,1,1])
    with col200:
        pass
    with col201:
        st.title("_§ § Dosimetria da Pena § §_")
    with col202:
        pass

    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #

    tab001,tab002,tab003 = st.columns(spec=[1,.75,1])
    with tab001:
        pass
    with tab002:
        idRandom = st.text_input("Informe ID",max_chars=4)
    with tab003:
        pass
    if st.button("Buscar", type="primary", use_container_width=True):
        # Conecta ao banco de dados
        conn = sqlite3.connect('cadastro.db')
        cursor = conn.cursor()

        # Consulta o banco de dados para verificar se o ID existe
        cursor.execute("SELECT * FROM delinquentes WHERE id = ?", (idRandom,))
        resultado = cursor.fetchone()

        conn.close()

        # Verifica se o ID foi encontrado
        if resultado:
            # Exibe os dados do registro encontrado
            st.success("Registro encontrado:")
            col100, col101,col102,col103,col104 = st.columns(spec=[1,.50,.50,1,1])
            with col100:
                # st.write(f"**ID:** {resultado[0]}")
            
                # st.write(f"**Data:** {resultado[1]}")
            
                # st.write(f"**Hora:** {resultado[2]}")
            
                st.write(f"**Nome Completo:** {resultado[3]}")
            with col101:
                st.write(f"**Nacionalidade:** {resultado[4]}")
            with col102:
                st.write(f"**Estado Civil:** {resultado[5]}")
            with col103:
                st.write(f"**Data de Nascimento:** {resultado[6]}")
            with col104:
                st.write(f"**Profissão:** {resultado[7]}")
            
            col105,col106,col107,col108,col109,col110 = st.columns(spec=[.75,1,.50,1,1,1])
            with col105:
                st.write(f"**CPF:** {resultado[8]}")
            with col106:                
                st.write(f"**Endereço:** {resultado[9]}")
            with col107:
                st.write(f"**Número:** {resultado[10]}")
            with col108:
                st.write(f"**Complemento:** {resultado[11]}")
            with col109:
                st.write(f"**Bairro:** {resultado[12]}")
            with col110:
                st.write(f"**Estado:** {resultado[13]}")
                
            col111,col112,col113,col114 = st.columns(spec=[.25,.50,.50,1])
            with col111:
                st.write(f"**Gênero:** {resultado[14]}")
            with col112:
                st.write(f"**Etnia:** {resultado[15]}")
            with col113:
                st.write(f"**Acusação:** {resultado[16]}")
            with col114:
                st.write(f"**Resumo:** {resultado[17]}")
    

    
# §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #

    

    col001,col002,col003 = st.columns(spec=[1,1,1])
    with col001:
        pass
    with col002:
    
        st.subheader("_§ § Fixação da Pena-Base § §_")
    with col003:
        pass

    basebox = 0
    atebox = 0
    agrbox = 0

    col1,col2 = st.columns(spec = [1,1])
    
    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #

    with col1 :

        culpabilidade = st.checkbox("culpabilidade")
        if culpabilidade:
            basebox += 1
        antecedentes = st.checkbox("Antecedentes ")
        if antecedentes:
            basebox += 1
        conduta_social = st.checkbox("Conduta Social")
        if conduta_social:
            basebox += 1
        Personalidade = st.checkbox("Personalidade do Agente")
        if Personalidade:
            basebox += 1
        

    with col2:

        motivos = st.checkbox("Motivos")
        if motivos:
            basebox += 1
        circunstancia = st.checkbox("Circunstâncias do Crime")
        if circunstancia:
            basebox += 1
        consequências = st.checkbox("Consequências do Crime")
        if consequências:
            basebox += 1
        comportamento_vitima = st.checkbox("Comportamento da Vítima")
        if comportamento_vitima:
            basebox += 1

   


    col3,col4 = st.columns(spec=[1,1])
    with col3:
        # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
        
            
        st.subheader("Causas Atenuantes",divider = "green")


        menoridade = st.checkbox(" menoridade ")
        if menoridade:
            atebox += 1
        confissao = st.checkbox(" confissão ")
        if confissao:
            atebox += 1
        desconhecimento_da_lei = st.checkbox(" desconhecimento da lei ")
        if desconhecimento_da_lei:
            atebox += 1

    with col4:
    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
        st.subheader("Causas Agravantes",divider = "red")
        
       
        Concurso_de_pessoas = st.checkbox(" Concurso de pessoas ")
        if Concurso_de_pessoas:
            agrbox += 1
        Reincidência = st.checkbox(" Reincidência ")
        if Reincidência:
            agrbox += 1
        Motivo_futil = st.checkbox(" Motivo fútil ")
        if Motivo_futil:
            agrbox += 1


    st.subheader(f"Pena Base ={basebox}")
    st.subheader(f"Atenuantes = {atebox}")
    st.subheader(f"Agravantes = {agrbox}")



    st.subheader("pena definitiva",divider = "blue")





    col5,col6,col7 = st.columns(spec=[1,1,1])
    with col5:
        pass
    with col6:

        if st.button("Calcular",type ="primary",use_container_width=True):
            
            st.success(f"Pena Final: {pena_final:.2f} anos",icon=":material/balance:")

    with col7:
        pass
    

        
