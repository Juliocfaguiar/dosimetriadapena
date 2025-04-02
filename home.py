import streamlit as st 



def app():
    
    #st.title("""""")
    st.markdown("")
    st.markdown("<h1 style='text-align: center; '>O que é Dosimetria da Pena ?</h1>", unsafe_allow_html=True)
    st.markdown("")
    st.markdown("<h5 style='text-align: justify; '>Em muitas situações no setor agrícola, garantir condições de operação seguras e otimizadas é uma preocupação essencial para engenheiros e operadores de máquinas agrícolas. No caso da colheita mecanizada da cana-de-açúcar, os operadores de colheitadeiras precisam ajustar diversos parâmetros para obter um desempenho eficiente, maximizando a produtividade e minimizando perdas.</h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: justify; '>No entanto, as condições da lavoura são altamente dinâmicas, com variações no tipo de solo, umidade, inclinação do terreno e densidade da plantação. Encontrar as configurações ideais para a colheitadeira em cada situação representa um grande desafio para os operadores. Ajustes incorretos podem resultar em perdas de cana, aumento do consumo de combustível e desgaste excessivo dos componentes da máquina. Em cenários mais críticos, podem ocorrer atolamentos, falhas mecânicas e até paradas não planejadas, comprometendo toda a operação agrícola. </h1>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns((1, 3, 1))       
    with c1:
            st.write("")
    with c2: 
            pass    
    with c3:
            st.write("")
    
    st.markdown("<h5 style='text-align: justify; '>Um Gêmeo Digital é uma representação virtual de um objeto físico, atualizada com dados em tempo real, aprendizado de máquina e simulações para auxiliar na tomada de decisões. No contexto da colheita da cana-de-açúcar, a criação de um Modelo de Gêmeo Digital permite simular e prever o comportamento da colheitadeira sob diferentes condições de operação. Com esse modelo, é possível avaliar como ajustes de velocidade, altura de corte, rotação dos extratores de impurezas e outros parâmetros afetam a eficiência da colheita.</h1>", unsafe_allow_html=True)
            
    st.markdown("<h5 style='text-align: justify; '>Além disso, ao conectar sensores instalados na colheitadeira a um Gêmeo Digital treinado, o sistema pode fornecer recomendações em tempo real para o operador. Dessa forma, a máquina pode ser ajustada dinamicamente para maximizar a produtividade e reduzir perdas, garantindo um corte mais eficiente e com menor impacto ambiental. O uso do Gêmeo Digital também possibilita a realização de simulações de manutenção preditiva, evitando falhas inesperadas e aumentando a vida útil dos equipamentos. </h1>", unsafe_allow_html=True)

    st.markdown("<h5 style='text-align: justify; '>Assim, a tecnologia de Gêmeo Digital aplicada à colheita da cana-de-açúcar não apenas melhora a eficiência operacional, mas também contribui para a sustentabilidade do setor agrícola, reduzindo desperdícios e otimizando o uso de recursos. Dessa maneira, engenheiros e operadores podem tomar decisões mais assertivas, garantindo maior produtividade e rentabilidade para o produtor.  </h1>", unsafe_allow_html=True)

