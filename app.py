# Importando bibliotecas
import streamlit as st
import pandas as pd

# Configurando título e nome da página
st.set_page_config(page_title='Análise Exploratória')
st.title('Bem-vindo à Análise Exploratória das Despesas de Viagem')

# Função de upload dos dados com armazenamento em cache
@st.cache_resource
def load_data():
    dados = pd.read_csv('dados.csv', sep=';')
    dados['PROPORCAO'] = dados['VALOREMPENHO'] / dados['PIB']
    return dados


# Persistindo dados para todas as sessões
dados = load_data()
st.session_state['dados'] = dados

# Definindo sidebar
with st.sidebar:
    st.header('Configurações Globais')
    if 'top_n' in st.session_state:
        default_top_n = st.session_state['top_n']
    else:
        default_top_n = 10

    top_n = st.number_input('Selecione o número de dados para exibir:', min_value=1, max_value=len(dados), value=default_top_n)
    st.session_state['top_n'] = top_n