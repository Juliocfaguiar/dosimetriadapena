import streamlit as st
import pandas as pd
import sqlite3
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from pdf import gerar_pdf


def app():
    if "resultado" not in st.session_state:
        st.session_state.resultado = None
    if "pena_inicial" not in st.session_state:
        st.session_state.pena_inicial = ""
    if "pena_base" not in st.session_state:
        st.session_state.pena_base = ""
    if "provisorio" not in st.session_state:
        st.session_state.provisorio = ""
    if "provisorio_pdf" not in st.session_state:
        st.session_state.provisorio_pdf = ""
    if "calculoFinalBase" not in st.session_state:
        st.session_state.calculoFinalBase = None
    if "final_resultAno" not in st.session_state:
        st.session_state.final_resultAno = None
    if "provAno" not in st.session_state:
        st.session_state.provAno = None
    if "pena_final_com_detração" not in st.session_state:
        st.session_state.pena_final_com_detração = ""
    if "pena_final_com_detração_pdf" not in st.session_state:
        st.session_state.pena_final_com_detração_pdf = ""
    if "totalDef_Anos" not in st.session_state:
        st.session_state.totalDef_Anos = None
    if "finalDef_result" not in st.session_state:
        st.session_state.finalDef_result = None

    

    # Variáveis locais
    pena_provisoria = "Não calculada"
    pena_definitiva = "Não calculada"

    # Atualiza variáveis com base no session_state
    if "provisorio" in st.session_state and st.session_state.provisorio:
        pena_provisoria = st.session_state.provisorio
    if "totalDef_split" in locals():
        pena_definitiva = f"{totalDef_Anos} ano(s) e {finalDef_result} mês(es)"

    # Lê o arquivo CSV com os crimes
    df = pd.read_csv("crimes.csv", sep=";")

    # Título da aplicação
    col200, col201, col202 = st.columns([.80, 1, .25])
    with col201:
        st.title("Dosimetria da Pena")

    # Input para buscar ID
    col900, col901, col902 = st.columns([1, .50, 1])
    with col901:
        
        idRandom = st.text_input("Informe ID", max_chars=5)
        if st.button("Buscar", type="primary", use_container_width=True):
            try:
                conn = sqlite3.connect("cadastro.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM delinquentes WHERE id = ?", (idRandom,))
                st.session_state.resultado = cursor.fetchone()
                conn.close()
            except sqlite3.Error as e:
                st.error(f"Erro ao acessar o banco de dados: {e}")
    col903, col904, col905 = st.columns([.15, 1, .15])
    with col904:
        # Exibir resultado da busca
        squirtle = st.container(border=True)
        with squirtle:
            if st.session_state.resultado:
                resultado = st.session_state.resultado
                
                col100, col101, col102, col103, col104 = st.columns(spec=[1, .50, .50, .50, .50])
                with col100:
                    st.write(f"**Nome Completo:** {resultado[3]}")
                with col101:
                    st.write(f"**Nacionalidade:** {resultado[4]}")
                with col102:
                    st.write(f"**Estado Civil:** {resultado[5]}")
                with col103:
                    st.write(f"**Nascimento:** {resultado[6]}")
                with col104:
                    st.write(f"**Profissão:** {resultado[7]}")
                col105, col106, col107, col108, col109, col110 = st.columns(spec=[.75, 1, .50, 1, 1, 1])
                with col105:
                    st.write(f"**CPF:** {resultado[8]}")
                with col106:
                    st.write(f"**Endereço:** {resultado[9]}")
                with col107:
                    st.write(f"**Número:** {resultado[10]}")
                with col108:
                    st.write(f"**Bairro:** {resultado[11]}")
                with col109:
                    st.write(f"**Cidade** {resultado[12]}")
                with col110:
                    st.write(f"**Estado:** {resultado[13]}")
                col111, col112, col113, col114 = st.columns(spec=[.25, .50, .50, 1])
                with col111:
                    st.write(f"**Gênero:** {resultado[14]}")
                with col112:
                    st.write(f"**Etnia:** {resultado[15]}")
                with col113:
                    st.write(f"**Acusação Art.:** {resultado[16]}")
                with col114:
                    st.write(f"**Resumo:** {resultado[17]}")

    col906, col907, col908 = st.columns([.50, 1, .50])
    with col907:
        # Fixação da Pena-Base
        col001, col002, col003 = st.columns(spec=[.70, 1, .25])
        with col002:
            st.subheader("Fixação da Pena-Base")
        
        Wartortle = st.container(border=True)
        with Wartortle:
            basebox = 0
            col1, col2 = st.columns(spec=[1, 1])
            with col1:
                culpabilidade = st.checkbox("Culpabilidade", key="culpabilidade", value=st.session_state.get("culpabilidade", False))
                if culpabilidade:
                    basebox += 1
                antecedentes = st.checkbox("Antecedentes", key="antecedentes", value=st.session_state.get("antecedentes", False))
                if antecedentes:
                    basebox += 1
                conduta_social = st.checkbox("Conduta Social", key="conduta_social", value=st.session_state.get("conduta_social", False))
                if conduta_social:
                    basebox += 1
                personalidade = st.checkbox("Personalidade do Agente", key="personalidade", value=st.session_state.get("personalidade", False))
                if personalidade:
                    basebox += 1
            with col2:
                motivos = st.checkbox("Motivos", key="motivos", value=st.session_state.get("motivos", False))
                if motivos:
                    basebox += 1
                circunstancias = st.checkbox("Circunstâncias do Crime", key="circunstancias", value=st.session_state.get("circunstancias", False))
                if circunstancias:
                    basebox += 1
                consequencias = st.checkbox("Consequências do Crime", key="consequencias", value=st.session_state.get("consequencias", False))
                if consequencias:
                    basebox += 1
                comportamento_vitima = st.checkbox("Comportamento da Vítima", key="comportamento_vitima", value=st.session_state.get("comportamento_vitima", False))
                if comportamento_vitima:
                    basebox += 1

        # Botão para calcular a pena base
        charmander = st.button("Calcular Pena Base", type="primary", use_container_width=True)
        if charmander:
            if 'resultado' in st.session_state and st.session_state.resultado:
                resultado = st.session_state.resultado
                for index, row in df.iterrows():
                    try:
                        filtered_row = df[df["art"].astype(str) == str(resultado[16])]
                        if not filtered_row.empty:
                            row = filtered_row.iloc[0]
                            if pd.notna(row["anoMax"]) and pd.notna(row["anoMin"]):
                                st.session_state.pena_inicial = f"Pena inicial de: {row['anoMin']} anos até {row['anoMax']} anos"
                                resultAno = (row["anoMax"] - row["anoMin"]) * 360
                                resultAno = resultAno * (basebox / 8)
                                resultAno = resultAno / 360
                                result_strAno = str(resultAno)
                                split_resultAno = result_strAno.split(".")
                                if len(split_resultAno) > 1 and split_resultAno[1] != 0:
                                    decimal_part = int(split_resultAno[1])
                                    final_resultAno = round((decimal_part / 100) * 12, 2)
                                    if final_resultAno == 0.6:
                                        final_resultAno = final_resultAno * 10
                                    calculoFinalBase = row["anoMin"] + int(split_resultAno[0])
                                    calculoFinalBase = int(calculoFinalBase)
                                    final_resultAno = int(final_resultAno)
                                    st.session_state.calculoFinalBase = calculoFinalBase
                                    st.session_state.final_resultAno = final_resultAno
                                    st.session_state.pena_base = f"Sentenciado a Pena base de: {calculoFinalBase} ano(s) e {final_resultAno} mês(es)"
                                    break
                    except KeyError as e:
                        st.error(f"Erro: A coluna {e} não foi encontrada no DataFrame.")
                        break
            else:
                st.error("Por favor, realize a busca antes de calcular a pena.")
            st.write(st.session_state.pena_inicial)
            st.write(st.session_state.pena_base)

        # Causas Atenuantes e Agravantes
        provbox = 0
        col3, col4 = st.columns(spec=[1, 1])
        with col3:
            st.subheader("Causas Atenuantes", divider="green")
            menoridade = st.checkbox("Menoridade", key="menoridade", value=st.session_state.get("menoridade", False))
            if menoridade:
                provbox += 1
            confissao = st.checkbox("Confissão", key="confissao", value=st.session_state.get("confissao", False))
            if confissao:
                provbox += 1
            desconhecimento_da_lei = st.checkbox("Desconhecimento da Lei", key="desconhecimento_da_lei", value=st.session_state.get("desconhecimento_da_lei", False))
            if desconhecimento_da_lei:
                provbox += 1
        with col4:
            st.subheader("Causas Agravantes", divider="red")
            concurso_de_pessoas = st.checkbox("Concurso de Pessoas", key="concurso_de_pessoas", value=st.session_state.get("concurso_de_pessoas", False))
            if concurso_de_pessoas:
                provbox += 1
            reincidencia = st.checkbox("Reincidência", key="reincidencia", value=st.session_state.get("reincidencia", False))
            if reincidencia:
                provbox += 1
            motivo_futil = st.checkbox("Motivo Fútil", key="motivo_futil", value=st.session_state.get("motivo_futil", False))
            if motivo_futil:
                provbox += 1

        # Botão para calcular a pena provisória
        if "calculoFinalBase" in st.session_state and "final_resultAno" in st.session_state:
            if st.session_state.calculoFinalBase is not None and st.session_state.final_resultAno is not None:
                diasAno = st.session_state.calculoFinalBase * 360
                diasMes = st.session_state.final_resultAno * 30
                totalDias = diasAno + diasMes
                Charmeleon = st.button("Calcular Pena Provisória", type="primary", use_container_width=True)
                if Charmeleon:
                    if provbox > 0:
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
                            provAno = int(splitProv_resultAno[0])
                            st.session_state.provAno = provAno
                            st.session_state.finalProv_resultAno = finalProv_resultAno
                            st.write(f"Pena Provisória é de: {splitProv_resultAno[0]} ano(s) e {finalProv_resultAno} mes(es)")
                            st.session_state.provisorio = f"Pena Provisória é de: {splitProv_resultAno[0]} ano(s) e {finalProv_resultAno} mes(es)"
                            st.session_state.provisorio_pdf = f" {splitProv_resultAno[0]} ano(s) e {finalProv_resultAno} mes(es)"

        # Pena Definitiva
        Minbox = 0
        Majbox = 0
        col5, col6 = st.columns(spec=[1, 1])
        if "provAno" in st.session_state and st.session_state.provAno is not None:
            provAno = st.session_state.provAno
        else:
            provAno = 0
        # if Charmeleon:
        with col5:
            st.subheader("Minorantes (Redução)", divider="green")
            primeiroMin = st.checkbox("1/6", key="primeiroMin", value=st.session_state.get("primeiroMin", False))
            if primeiroMin:
                Minbox += 1 / 6
            segundoMin = st.checkbox("1/3", key="segundoMin", value=st.session_state.get("segundoMin", False))
            if segundoMin:
                Minbox += 1 / 3
            terceiroMin = st.checkbox("1/2", key="terceiroMin", value=st.session_state.get("terceiroMin", False))
            if terceiroMin:
                Minbox += 1 / 2
            quartoMin = st.checkbox("2/3", key="quartoMin", value=st.session_state.get("quartoMin", False))
            if quartoMin:
                Minbox += 2 / 3
            quintoMin = st.checkbox("1", key="quintoMin", value=st.session_state.get("quintoMin", False))
            if quintoMin:
                Minbox += 1
        with col6:
            st.subheader("Majorantes (Aumento)", divider="red")
            primeiroMaj = st.checkbox("1/6", key="primeiroMaj", value=st.session_state.get("primeiroMaj", False))
            if primeiroMaj:
                Majbox += 1 / 6
            segundoMaj = st.checkbox("1/3", key="segundoMaj", value=st.session_state.get("segundoMaj", False))
            if segundoMaj:
                Majbox += 1 / 3
            terceiroMaj = st.checkbox("1/2", key="terceiroMaj", value=st.session_state.get("terceiroMaj", False))
            if terceiroMaj:
                Majbox += 1 / 2
            quartoMaj = st.checkbox("2/3", key="quartoMaj", value=st.session_state.get("quartoMaj", False))
            if quartoMaj:
                Majbox += 2 / 3
            quintoMaj = st.checkbox("1", key="quintoMaj", value=st.session_state.get("quintoMaj", False))
            if quintoMaj:
                Majbox += 1

        if provAno > 0:
            defAnos = provAno * 360
            defMeses = float(st.session_state.finalProv_resultAno) * 30
            totalDef_Dias = defAnos + defMeses
            if st.button("Calcular Pena Definitiva", type="primary", use_container_width=True):
                if Minbox != 0:
                    totalMinbox = totalDef_Dias * Minbox
                    totalDef = totalDef_Dias - totalMinbox
                    totalDef_Anos = totalDef / 360
                    totalDef_Anos = str(totalDef_Anos)
                    totalDef_split = totalDef_Anos.split(".")
                    if len(totalDef_split) > 1 and totalDef_split[1] != 0:
                        decimalDef_part = int(totalDef_split[1])
                        finalDef_result = round(decimalDef_part / 1000000000000000, 2)
                        finalDef_result = int(finalDef_result)
                        totalDef_Anos = int(totalDef_split[0])
                        st.write(f"Definitiva Anos: {totalDef_Anos} e {finalDef_result} meses")
                    else:
                        st.write("A parte decimal é zero, não é possível realizar o cálculo.")
                if Majbox != 0:
                    totalMajbox = totalDef_Dias * Majbox
                    totalDef = totalDef_Dias + totalMajbox
                    totalDef_Anos = totalDef / 360
                    totalDef_Anos = str(totalDef_Anos)
                    totalDef_split = totalDef_Anos.split(".")
                    if len(totalDef_split) > 1 and totalDef_split[1] != 0:
                        decimalDef_part = int(totalDef_split[1])
                        finalDef_result = round(decimalDef_part / 1000000000000000, 2)
                        finalDef_result = int(finalDef_result)
                        totalDef_Anos = int(totalDef_split[0])

                        st.session_state.finalDef_result = finalDef_result
                        st.session_state.totalDef_Anos = totalDef_Anos
                        st.session_state.pena_definitiva = f"Sentenciado a Pena base de: {totalDef_Anos} ano(s) e {finalDef_result} mês(es)"

                        
                        st.write(f"Definitiva Anos: {totalDef_Anos} e {finalDef_result} meses")
                    else:
                        st.write("A parte decimal é zero, não é possível realizar o cálculo.")


        if "definitiva_ano" not in st.session_state:
            st.session_state.definitiva_ano = 0
        if "definitiva_mes" not in st.session_state:    
            st.session_state.definitiva_mes = 0
        if "definitiva_dias" not in st.session_state:
            st.session_state.definitiva_dias = 0
        # Detração
        col1, col2, col3 = st.columns(3)
        with col1:
            anos_detraidos = st.number_input("Anos detraídos", min_value=0, step=1, value=0)
        with col2:
            meses_detraidos = st.number_input("Meses detraídos", min_value=0, max_value=11, step=1, value=0)
        with col3:
            dias_detraidos = st.number_input("Dias detraídos", min_value=0, max_value=29, step=1, value=0)

        if st.button("Aplicar Detração", type="secondary", use_container_width=True):
            # Calcula os dias totais da pena definitiva
            dias_totais_definitiva = (

                # st.session_state.definitiva_ano * 360 +
                # st.session_state.definitiva_mes * 30 +
                # st.session_state.definitiva_dias

                st.session_state.totalDef_Anos * 360 +
                st.session_state.finalDef_result * 30
            )
            # Calcula os dias totais detraídos
            dias_detraidos_total = (
                anos_detraidos * 360 + meses_detraidos * 30 + dias_detraidos
            )

            
            # Calcula o resultado final após a detração
            dias_resultado = dias_totais_definitiva - dias_detraidos_total
            if dias_resultado < 0:
                dias_resultado = 0
            anos_finais = dias_resultado // 360
            meses_finais = (dias_resultado % 360) // 30
            dias_finais = (dias_resultado % 360) % 30
            st.session_state.pena_final_com_detração = (
                f"Pena final com detração: {anos_finais} ano(s), "
                f"{meses_finais} mês(es) e {dias_finais} dia(s)"
                
            )
            st.session_state.pena_final_com_detração_pdf = (
                f" {anos_finais} ano(s), "
                f"{meses_finais} mês(es) e {dias_finais} dia(s)"
            )
            st.success(f"✅ {st.session_state.pena_final_com_detração}")


        # Botão para gerar e baixar o PDF
        if st.button("Gerar PDF", type="primary", use_container_width=True):
            if "resultado" in st.session_state and st.session_state.resultado:
                resultado = st.session_state.resultado
                # pena_provisoria = st.session_state.provisorio if "provisorio" in st.session_state else "Não calculada"
                pena_provisoria_pdf = st.session_state.provisorio_pdf if "provisorio" in st.session_state else "Não calculada"
                # pena_definitiva = st.session_state.pena_final_com_detração if "pena_final_com_detração" in st.session_state else "Não calculada"
                pena_definitiva_pdf = st.session_state.pena_final_com_detração_pdf if "pena_final_com_detração" in st.session_state else "Não calculada"
    
                # Gera o PDF
                pdf_buffer = gerar_pdf(resultado, pena_provisoria_pdf, pena_definitiva_pdf).getvalue()
                
                # Botão para download do PDF
                st.download_button(
                    label="Baixar PDF",
                    data=pdf_buffer,
                    file_name="relatorio_sentenca.pdf",
                    mime="application/pdf",
                    key="download_pdf_button"
                )
            else:
                st.error("Por favor, realize o cálculo da pena antes de gerar o PDF.")
                



    
    # totalDias_MinMaj = 





    
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
    
    