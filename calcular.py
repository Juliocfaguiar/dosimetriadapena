import streamlit as st
import pandas as pd
import sqlite3



def app():
    if "resultado" not in st.session_state:
        st.session_state.resultado = None
    
    


    df = pd.read_csv("crimes.csv",sep=";")

  

    col200, col201,col202 = st.columns([1,1,1])
    with col200:
        pass
    with col201:
        st.title("_§ § Dosimetria da Pena § §_")
    with col202:
        pass

    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
    
    col900,col901,col902 = st.columns(spec=[1,.75,1])
    with col900:
        pass
    with col901:
        idRandom = st.text_input("Informe ID",max_chars=4)
    with col902:
        pass
    
    # Botão de busca
    if st.button("Buscar", type="primary", use_container_width=True):
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
    # Verifica se há um resultado salvo no estado
    if st.session_state.resultado:
        resultado = st.session_state.resultado
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
            st.write(f"**Acusação Art.:** {resultado[16]}")
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
    provbox = 0

    col1,col2 = st.columns(spec = [1,1])
    
    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #

    with col1 :

        culpabilidade = st.checkbox("Culpabilidade", key="culpabilidade")
        if culpabilidade:
            basebox += 1
        antecedentes = st.checkbox("Antecedentes", key="antecedentes")
        if antecedentes:
            basebox += 1
        conduta_social = st.checkbox("Conduta Social", key="conduta_social")
        if conduta_social:
            basebox += 1
        personalidade = st.checkbox("Personalidade do Agente", key="personalidade")
        if personalidade:
            basebox += 1
        

    with col2:

        motivos = st.checkbox("Motivos", key="motivos")
        if motivos:
            basebox += 1
        circunstancias = st.checkbox("Circunstâncias do Crime", key="circunstancias")
        if circunstancias:
            basebox += 1
        consequencias = st.checkbox("Consequências do Crime", key="consequencias")
        if consequencias:
            basebox += 1
        comportamento_vitima = st.checkbox("Comportamento da Vítima", key="comportamento_vitima")
        if comportamento_vitima:
            basebox += 1

   
    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
    # calculo da pena Base em anos
    if st.button("Calcular Pena Base", type="primary", use_container_width=True):
        # Verifica se o resultado foi definido
        if 'resultado' in st.session_state and st.session_state.resultado:
            resultado = st.session_state.resultado

            # Itera sobre o DataFrame para encontrar a linha correspondente
            for index, row in df.iterrows():
                try:
                    # Filtra o DataFrame para encontrar a linha correspondente
                    filtered_row = df[df["art"].astype(str) == str(resultado[16])]

                    if not filtered_row.empty:
                        # Obtém a primeira linha correspondente
                        row = filtered_row.iloc[0]
                        if pd.notna(row["anoMax"]) and pd.notna(row["anoMin"]):
                            # Calcula a pena inicial
                            st.session_state.pena_inicial = f"Pena inicial de: {row['anoMin']} anos até {row['anoMax']} anos"
                            # st.write(st.session_state.pena_inicial)

                            # Calcula a pena base
                            resultAno = (row["anoMax"] - row["anoMin"]) * 360
                            resultAno = resultAno * (basebox / 8)
                            resultAno = resultAno / 360
                            result_strAno = str(resultAno)
                            split_resultAno = result_strAno.split(".")

                            # st.write(f"separar {split_resultAno}")
                            if len(split_resultAno) > 1 and split_resultAno[1] != 0:
                                decimal_part = int(split_resultAno[1])

                                final_resultAno = round((decimal_part / 100) * 12, 2)
                                if final_resultAno == 0.6:
                                    final_resultAno = final_resultAno * 10
                                calculoFinalBase = row["anoMin"] + int(split_resultAno[0])
                                calculoFinalBase = int(calculoFinalBase)
                                final_resultAno = int(final_resultAno)

                                # Salva os valores no st.session_state
                                st.session_state.calculoFinalBase = calculoFinalBase
                                st.session_state.final_resultAno = final_resultAno

                                # Salva a mensagem da pena base no session_state
                                st.session_state.pena_base = f"Sentenciado a Pena base de: {calculoFinalBase} ano(s) e {final_resultAno} mês(es)"
                                # st.write(st.session_state.pena_base)
                                break
                except KeyError as e:
                    st.error(f"Erro: A coluna {e} não foi encontrada no DataFrame.")
                    break
        else:
            st.error("Por favor, realize a busca antes de calcular a pena.")
    

    # Exibe as mensagens salvas no session_state, se existirem
    # if "pena_inicial" in st.session_state:
    st.write(st.session_state.pena_inicial)

    # if "pena_base" in st.session_state:
    st.write(st.session_state.pena_base)
        
    col3,col4 = st.columns(spec=[1,1])
    with col3:
        # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #       
            
        st.subheader("Causas Atenuantes",divider = "green")

        menoridade = st.checkbox("Menoridade", key="menoridade")
        if menoridade:
            provbox += 1
        confissao = st.checkbox("Confissão", key="confissao")
        if confissao:
            provbox += 1
        desconhecimento_da_lei = st.checkbox("Desconhecimento da Lei", key="desconhecimento_da_lei")
        if desconhecimento_da_lei:
            provbox += 1

    with col4:
    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
        st.subheader("Causas Agravantes",divider = "red")
        
    
        concurso_de_pessoas = st.checkbox("Concurso de Pessoas", key="concurso_de_pessoas")
        if concurso_de_pessoas:
            provbox += 1
        reincidencia = st.checkbox("Reincidência", key="reincidencia")
        if reincidencia:
            provbox += 1
        motivo_futil = st.checkbox("Motivo Fútil", key="motivo_futil")
        if motivo_futil:
            provbox += 1


# §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
    # calculo da pena Provisória em anos
    
    if "calculoFinalBase" in st.session_state and "final_resultAno" in st.session_state:
        if st.session_state.calculoFinalBase is not None and st.session_state.final_resultAno is not None:
            # Realiza os cálculos apenas se os valores não forem None
            diasAno = st.session_state.calculoFinalBase * 360
            diasMes = st.session_state.final_resultAno * 30
            totalDias = diasAno + diasMes
              #################################
            
        if st.button("Calcular Pena Provisória", type="primary", use_container_width=True):
        # Exemplo de cálculo adicional
            if provbox > 0:  # Certifique-se de que provbox não seja zero para evitar divisão por zero
                totalDias_provBox = totalDias * (provbox / 6)                
                Provisorio = totalDias_provBox / 360                 
                Provisorio = Provisorio * 12                              
                Provisorio = int(Provisorio)                     
                ProvisorioTotal = totalDias + (Provisorio * 30)                
                ProvisorioTotal = ProvisorioTotal / 360                
                ProvisorioTotal = str(ProvisorioTotal)
                splitProv_resultAno = ProvisorioTotal.split(".")
                if len(splitProv_resultAno) > 1 and splitProv_resultAno[1] != 0:
                    decimalProv_part = int(splitProv_resultAno[1])                    
                    finalProv_resultAno = (decimalProv_part * 12)
                    finalProv_resultAno = round(finalProv_resultAno / 1000000000000000, 2)
                    finalProv_resultAno = int(finalProv_resultAno)
                    st.write(f"Pena Provisória é de  : {splitProv_resultAno[0]} ano(s) e {finalProv_resultAno} mes(es)")
                    st.session_state.provisorio = f"Pena Provisória é de  : {splitProv_resultAno[0]} ano(s) e {finalProv_resultAno} mes(es)"
                    
# §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #

    Minbox = 0
    Majbox = 0

    
    
    # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #

    col5,col6 = st.columns(spec=[1,1])
    with col5:
        # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #       
            
        st.subheader("Minorantes (Redução)",divider = "green")

        primeiroMin = st.checkbox("-1/3", key="primeiroMin")
        if primeiroMin:
            Minbox -= 1/3
        
        segundoMin = st.checkbox("-2/3", key="segundoMin")
        if segundoMin:
            Minbox -= 2/3
        terceiroMin = st.checkbox("-1/2", key="terceiroMin")
        if terceiroMin:
            Minbox -= 1/2
        st.write(f"MinBox : {Minbox}")
    with col6:
    # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
        st.subheader("Majorantes (Aumento)",divider = "red")
        
    
        primeiroMaj = st.checkbox("+1/3 ", key="primeiroMaj")
        if primeiroMaj:
            Majbox += 1/3
       
        segundoMaj = st.checkbox("+2/3", key="segundoMaj")
        if segundoMaj:
            Majbox += 2/3
        terceiroMaj = st.checkbox("+1/2", key="terceiroMaj")
        if terceiroMaj:
            Majbox += 1/2
    st.write(f"Majbox : {Majbox}")








    
    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
    

                            # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
                            #  calculo de pena em meses

            #         if pd.notna(row["mesMax"]) and pd.notna(row["mesMin"]):
            #             st.write(f"pena de : {row['mesMin']} até {row['mesMax']}")
            #             resultMes = (row["mesMax"] - row["mesMin"]) * 30
            #             resultMes = resultMes * (basebox / 8)
            #             st.write(f"150 * (2/8) {resultMes}")
            #             resultMes = round(resultMes / 360 ,2)
            #             st.write(f"37,5/360  =  {resultMes}")
            #             resultMes = row["mesMin"] + resultMes 
            #             result_strMes = str(resultMes)
            #             st.write(f"mesesesese {resultMes}")
            #             split_result = result_strMes.split(".")
            #             if len(split_result) > 0 and int(split_result[0]) != 0:
            #                 st.write(f"Resultado: {split_result[0]} mes(es)")
            #             if len(split_result) > 1 and split_result[1] != 0:
            #                 decimal_part = int(split_result[1])
            #                 st.write(f"Rhuehuehuehuehue {decimal_part} dias")
            #                 final_result = round((decimal_part )/10 * 30, 1)
                            
                            
            #                 final_result = int(final_result)
            #                 st.write(f"hahahahaah{final_result} dias")
            #                 calculoFinal = row["mesMin"] + final_result
            #                 st.write(f"Sentenciado a : {calculoFinal} mes(es) e {final_result} dia(s)")
            #             break
                        
    # for index, row in df.iterrows():
    #     try:
            
    #         if str(resultado[16]) in df['art'].astype(str).values:

    #             print(f"Artigo encontrado: {row['art']}")
                

    #             if pd.notna(row['anoMax']) and pd.notna(row['anoMin']):
    #                 result = (row['anoMax'] - row['anoMin']) * 360 
    #                 if mewTwo:
    #                     if basebox > 0:
    #                         result = result * basebox/8

    #                         print(f"Resultado: {result}")
    #                         breakpoint()
    #                         result = result / 360
                            
    #                         result_str = str(result)
    #                         split_result = result_str.split(".")
                            
    #                         if len(split_result) > 0 and int(split_result[0]) != 0:
    #                             print(f"O resultado final é: {int(split_result[0])} ano(s)")
    #                         else:
    #                             print("A parte inteira do resultado é zero.")
                                
    #                     else:
    #                         print("anoMax ou anoMin não possuem valor, não é possível realizar o cálculo.")
    #     except KeyError as e:
    #         print(f"Erro: A coluna {e} não foi encontrada no DataFrame.")
    #         break

    # for index, row in df.iterrows():
    #     try:
    #         if row['art'] == 155:
    #             if pd.notna(row['anoMax']) and pd.notna(row['anoMin']):
    #                 result = (row['anoMax'] - row['anoMin']) * 360 
    #                 result = result * 2/8
    #                 result = result / 360
                    
    #                 result_str = str(result)
    #                 split_result = result_str.split(".")
                    
    #                 if len(split_result) > 1 and split_result[1] != '0':
    #                     decimal_part = int(split_result[1])
    #                     final_result = round((decimal_part / 100) * 12, 2)
    #                     final_result = round(final_result*10, 2)
    #                     final_result = int(final_result)
    #                     print(f"O resultado final é: {final_result} mes(es)")
    #                 else:
    #                     print("A parte decimal é zero, não é possível realizar o cálculo.")
                        
    #             else:
    #                 print("anoMax ou anoMin não possuem valor, não é possível realizar o cálculo.")
    #     except KeyError as e:
    #         print(f"Erro: A coluna {e} não foi encontrada no DataFrame.")
    #         break
    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #

    # col5,col6,col7 = st.columns(spec=[1,1,1])
    # with col5:
    #     pass
    # with col6:

    #     if st.button("Calcular",type ="primary",use_container_width=True):
            
    #         st.success(f"Pena Definitiva: {pena_final:.2f} anos",icon=":material/balance:")

    # with col7:
    #     pass
    
    
