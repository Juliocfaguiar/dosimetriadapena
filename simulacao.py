import streamlit as st
import pandas as pd
import pydeck as pdk
import time
import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    # Fórmula de Haversine para calcular a distância em metros
    R = 6371000  # Raio da Terra em metros
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distancia = R * c  # Distância em metros
    return distancia

def app():
    col1, col2, col3 = st.columns([.80, 1, .75], vertical_alignment='center')
    with col2:
        
        st.title("Sistema de Medida Protetiva")
    col4, col5, col6 = st.columns([.94, 1, 1], vertical_alignment='center')
    with col5:
        
        st.title(":blue[Simulação de Identificação]")

    # Lê o arquivo CSV
    dfGPS = pd.read_csv("teste_GPS.csv", sep=";")

    # Verifica se o DataFrame está vazio
    if dfGPS.empty:
        st.error("O arquivo CSV está vazio ou não contém dados válidos.")
        return

    # Divide os dados por pessoa
    pessoa1 = dfGPS[dfGPS["pessoa"] == "Pessoa_1"].reset_index(drop=True)
    pessoa2 = dfGPS[dfGPS["pessoa"] == "Pessoa_2"].reset_index(drop=True)

    # Verifica se os dados de ambas as pessoas estão disponíveis
    if pessoa1.empty or pessoa2.empty:
        st.error("Os dados de uma ou ambas as pessoas estão ausentes no arquivo CSV.")
        return

    # Configuração inicial do mapa
    view_state = pdk.ViewState(
        latitude=pessoa1.loc[0, 'lat'],  # Centraliza no primeiro ponto da pessoa 1
        longitude=pessoa1.loc[0, 'lon'],
        zoom=14,
        pitch=0
    )

    # Cria um espaço reservado para o gráfico
    map_placeholder = st.empty()

    # Inicializa o índice de localização
    index = 0

    # Loop para simular o movimento
    while index < len(pessoa1) and index < len(pessoa2):
        # Atualiza as localizações atuais
        current_data = pd.DataFrame({
            'lat': [pessoa1.loc[index, 'lat'], pessoa2.loc[index, 'lat']],
            'lon': [pessoa1.loc[index, 'lon'], pessoa2.loc[index, 'lon']],
            'pessoa': ['Pessoa_1', 'Pessoa_2']
        })

        # Calcula a distância entre os dois pontos
        distancia = calcular_distancia(
            pessoa1.loc[index, 'lat'], pessoa1.loc[index, 'lon'],
            pessoa2.loc[index, 'lat'], pessoa2.loc[index, 'lon']
        )

        # Exibe a distância no Streamlit
        st.write(f"Distância entre Pessoa_1 e Pessoa_2: {distancia:.2f} metros")

        # Verifica se a distância é menor ou igual ao limite (exemplo: 100 metros)
        if distancia <= 100:
            st.warning("Alerta! Quebra de distanciamento detectada!")

        # Criação da camada para as localizações
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=current_data,
            get_position='[lon, lat]',
            get_fill_color='[255, 0, 0, 100]',  # Adiciona transparência
            get_radius=100,
            pickable=True
        )

        # Atualiza o gráfico no espaço reservado
        map_placeholder.pydeck_chart(pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip={"text": "{pessoa}: Lat {lat}, Lon {lon}"}
        ))

        # Incrementa o índice e aguarda 5 segundos
        index += 1
        time.sleep(5)