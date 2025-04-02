import streamlit as st
import pandas as pd


def app():
    
    
    # Carrega o dataset
    # df = pd.read_csv('dosimetria_da_pena.csv')

    # Inicializa variáveis de sessão
    if 'pena_base' not in st.session_state:
        st.session_state.pena_base = None
    if 'pena_final' not in st.session_state:
        st.session_state.pena_final = None

    # Função para calcular a pena-base
    def calcular_pena_base(culpabilidade, antecedentes, conduta_social, motivos, consequencias, comportamento_vitima):
        # Definir pesos para cada fator (ajustáveis conforme jurisprudência)
        pesos = {
            "culpabilidade": 0.2,
            "antecedentes": 0.15,
            "conduta_social": 0.15,
            "motivos": 0.1,
            "consequencias": 0.25,
            "comportamento_vitima": 0.15
        }
        
        # Normalizar as entradas (ex.: escala de 0 a 10)
        fatores = {
            "culpabilidade": culpabilidade / 10,
            "antecedentes": antecedentes / 10,
            "conduta_social": conduta_social / 10,
            "motivos": motivos / 10,
            "consequencias": consequencias / 10,
            "comportamento_vitima": comportamento_vitima / 10
        }
        
        # Calcular a pena-base
        pena_base = sum(fatores[fator] * pesos[fator] for fator in pesos)
        return pena_base * 30  # Escalar para anos (ex.: máximo de 30 anos)

    # Função para aplicar atenuantes e agravantes
    def aplicar_atenuantes_agravantes(pena_base, atenuantes, agravantes):
        # Frações típicas para atenuantes e agravantes (ajustáveis conforme jurisprudência)
        fracao_atenuante = 0.1
        fracao_agravante = 0.1
        
        # Aplicar atenuantes
        pena = pena_base - (pena_base * len(atenuantes) * fracao_atenuante)
        
        # Aplicar agravantes
        pena = pena + (pena_base * len(agravantes) * fracao_agravante)
        
        return max(0, pena)  # Garantir que a pena não seja negativa

    # Função para aplicar causas especiais de aumento ou diminuição
    def aplicar_causas_especiais(pena_final, causas_aumento, causas_diminuicao):
        # Frações típicas para causas especiais (ajustáveis conforme legislação)
        fracao_aumento = 0.2
        fracao_diminuicao = 0.2
        
        # Aplicar causas de aumento
        pena = pena_final + (pena_final * len(causas_aumento) * fracao_aumento)
        
        # Aplicar causas de diminuição
        pena = pena - (pena_final * len(causas_diminuicao) * fracao_diminuicao)
        
        return max(0, pena)  # Garantir que a pena não seja negativa

    col001,col002,col003 = st.columns(spec=[1,1,1])
    with col001:
        pass
    with col002:
        st.title("Dosimetria da Pena")
        st.subheader("_§ § Fixação da Pena-Base § §_")
    with col003:
        pass
    col1,col2 = st.columns(spec = [1,1])
    # Opções
    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #

    with col1 :

        culpabilidade = st.slider("Culpabilidade (0-10):", 0, 10, 5)
        antecedentes = st.slider("Antecedentes (0-10):", 0, 10, 5)
        conduta_social = st.slider("Conduta Social (0-10):", 0, 10, 5)
    with col2:

        motivos = st.slider("Motivos (0-10):", 0, 10, 5)
        consequencias = st.slider("Consequências do Crime (0-10):", 0, 10, 5)
        comportamento_vitima = st.slider("Comportamento da Vítima (0-10):", 0, 10, 5)


    st.session_state.pena_base = calcular_pena_base(culpabilidade, antecedentes, conduta_social, motivos, consequencias, comportamento_vitima)


    col3,col4 = st.columns(spec=[1,1])
    with col3:
        # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
        if st.session_state.pena_base is not None:
            
            st.subheader("Atenuantes e Agravantes")
            pena_base = st.number_input("Pena-Base (anos):", min_value=0.0, value=st.session_state.pena_base)
            atenuantes = st.multiselect("Atenuantes:", ["Confissão", "Arrependimento", "Primariedade"])
            agravantes = st.multiselect("Agravantes:", ["Reincidência", "Crime Hediondo", "Uso de Violência"])
            
            
            st.session_state.pena_final = aplicar_atenuantes_agravantes(pena_base, atenuantes, agravantes)
            

    with col4:
    # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ # # §§§§§§§§§§§§§§§§ #
        st.subheader("Causas Especiais")
        if st.session_state.pena_final is None:
            
            st.warning("Por favor, aplique os Atenuantes e Agravantes primeiro.")
        else:
            pena_final = st.number_input("Pena Após Atenuantes e Agravantes (anos):", min_value=0.0, value=st.session_state.pena_final)
            causas_aumento = st.multiselect("Causas de Aumento:", ["Participação de Menor", "Crime Continuado"])
            causas_diminuicao = st.multiselect("Causas de Diminuição:", ["Arrependimento Posterior", "Crime Privilegiado"])
    col5,col6,col7 = st.columns(spec=[1,1,1])
    with col5:
        pass
    with col6:

        if st.button("Calcular",type ="primary",use_container_width=True):
            pena_final = aplicar_causas_especiais(pena_final, causas_aumento, causas_diminuicao)
            st.success(f"Pena Final: {pena_final:.2f} anos",icon=":material/balance:")

    with col7:
        pass

