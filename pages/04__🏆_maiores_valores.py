# Importando bibliotecas
import streamlit as st
import plotly.express as px

# Header da página
st.header('Maiores Valores')

# Verificação se os dados estão carregados em state
if 'dados' not in st.session_state:
    st.error('Os dados não foram carregados')
else:
    top_n = st.session_state.get('top_n', 10)
    dados = st.session_state['dados']

    col1, col2, col3 = st.columns(3)

    with col1:
        m_empenho = dados.nlargest(top_n, 'VALOREMPENHO')
        fig1 = px.bar(m_empenho, x='MUNICIPIO', y='VALOREMPENHO', title='Maiores Empenhos')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        m_pibs = dados.nlargest(top_n, 'PIB')
        fig2 = px.pie(m_pibs, values='PIB', names='MUNICIPIO', title='Maiores PIBs')
        st.plotly_chart(fig2, use_container_width=True)

    with col3:
        m_prop = dados.nlargest(top_n, 'PROPORCAO')
        fig3 = px.bar(m_prop, x='MUNICIPIO', y='PROPORCAO', title='Maiores Gastos em Proporção ao PIB')
        st.plotly_chart(fig3, use_container_width=True)