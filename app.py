import streamlit as st 


st.set_page_config(layout="wide")


st.title('Statistics')


col1,col2,col3=st.columns([2,2,1])
with col1:
    with st.expander('Base de datos'):
        st.file_uploader('Base de datos (xls,xlsx)')
        st.button('Enviar',key=198)
with col2:
    with st.expander('Protocolo de tesis'):
        st.file_uploader('Protocolo de tesis (Docx,pdf,txt)')
        st.button('Enviar',key=234)
with col3:
    st.text_area('Contacto')
    st.button('Enviar')