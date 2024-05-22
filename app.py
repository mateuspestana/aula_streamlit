import streamlit as st

st.title('Salut')

with st.sidebar:
  st.header('Salut')
  st.write('Seu aplicativo de dicas de saúde!')
  st.caption('Criado por Matheus C. Pestana')

st.write('Nosso aplicativo tem como foco oferecer dicas maravilhosas sobre corrida, nutrição e notícias de saúde! Escolha a opção abaixo!') 
tab_corrida, tab_nutri, tab_news = st.tabs(["Corrida de Rua", "Nutrição", "Notícias"])
