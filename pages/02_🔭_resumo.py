# Importando bibliotecas
import streamlit as st

# Header da página
st.header('Resumo dos Dados')

# Verificação se os dados estão carregados em state
if 'dados' not in st.session_state:
    st.error('Os dados não foram carregados')
else:
    dados = st.session_state['dados'].describe().reset_index()
    st.write(dados)