import streamlit as st

def calc_pace(distancia, tempo_min, tempo_seg):
  tempo_total_segundos = (tempo_min * 60) + tempo_seg
  pace_segundos_por_km = tempo_total_segundos / distancia
  pace_min = int(pace_segundos_por_km // 60)
  pace_seg = int(pace_segundos_por_km % 60)
  return pace_min, pace_seg

st.title('Salut')

with st.sidebar:
  st.header('Salut')
  st.write('Seu aplicativo de dicas de saúde!')
  st.caption('Criado por Matheus C. Pestana')

st.write('Nosso aplicativo tem como foco oferecer dicas maravilhosas sobre corrida, nutrição e notícias de saúde! Escolha a opção abaixo!') 
tab_corrida, tab_nutri, tab_news = st.tabs(["Corrida de Rua", "Nutrição", "Notícias"])

with tab_corrida:
  with st.form('calc_pace_form'):
    st.write('Calculadora de Pace')
    distancia = st.number_input('Insira quantos km você correu', 1, 42)
    tempo_min = st.number_input('Insira em quantos minutos você correu', 1, 59)
    tempo_seg = st.number_input('Insira em quantos segundos você correu', 0, 59)
    enviar = st.form_submit_button('Enviar')
    if enviar:
      pace_min, pace_seg = calc_pace(distancia, tempo_min, tempo_seg)
      st.write(f'Seu pace é de {pace_min} minutos e {pace_seg} segundos por km')

  
  
