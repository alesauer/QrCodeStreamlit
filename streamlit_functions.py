"""

Principais funções e métodos do Streamlit

Este arquivo contém exemplos e explicações das principais funções do Streamlit
para criação de aplicativos web com Python.
"""

import streamlit as st

# 1. Elementos de Texto
st.title('Título da Página')  # Título principal
st.header('Cabeçalho')  # Cabeçalho de seção
st.subheader('Subcabeçalho')  # Subcabeçalho
st.text('Texto simples')  # Texto formatado
st.markdown('**Markdown** suportado')  # Markdown
st.latex(r'\sqrt{a^2 + b^2}')  # Equações matemáticas

# 2. Elementos de Entrada de Dados
text_input = st.text_input('Campo de texto')  # Input de texto
number_input = st.number_input('Número')  # Input numérico
date_input = st.date_input('Data')  # Seletor de data
file_uploader = st.file_uploader('Upload de arquivo')  # Upload de arquivos
camera_input = st.camera_input('Tirar foto')  # Captura de câmera

# 3. Elementos de Seleção
selectbox = st.selectbox('Selecione', ['Opção 1', 'Opção 2'])  # Select box
multiselect = st.multiselect('Multi seleção', ['A', 'B', 'C'])  # Multi seleção
radio = st.radio('Escolha', ['Sim', 'Não'])  # Botões de rádio
slider = st.slider('Slider', 0, 100)  # Controle deslizante

# 4. Exibição de Dados
st.dataframe(pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}))  # DataFrame
st.table([[1, 2], [3, 4]])  # Tabela estática
st.json({'key': 'value'})  # Exibição de JSON
st.metric('Métrica', 42, 2)  # Exibição de métrica

# 5. Elementos de Layout
col1, col2 = st.columns(2)  # Colunas
with col1:
    st.write('Coluna 1')
with col2:
    st.write('Coluna 2')

tab1, tab2 = st.tabs(['Tab 1', 'Tab 2'])  # Abas
with tab1:
    st.write('Conteúdo Tab 1')
with tab2:
    st.write('Conteúdo Tab 2')

# 6. Controles de Estado
if st.button('Clique aqui'):  # Botão
    st.write('Botão clicado!')

st.checkbox('Checkbox')  # Checkbox
st.progress(0.5)  # Barra de progresso
st.spinner()  # Spinner de carregamento

# 7. Exibição de Mídia
st.image('image.png')  # Exibição de imagens
st.audio('audio.mp3')  # Exibição de áudio
st.video('video.mp4')  # Exibição de vídeo

# 8. Controle de Sessão
if 'counter' not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1
st.write('Contador:', st.session_state.counter)

# 9. Outras Funções Úteis
st.cache_data  # Cache de dados
st.cache_resource  # Cache de recursos
st.experimental_rerun()  # Recarregar aplicativo
st.set_page_config(page_title='Título', layout='wide')  # Configurações da página
