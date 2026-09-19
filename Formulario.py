import streamlit as st 

def formulario():
    st.title("Formulario")
    st.divider()

    with st.form("contacto",clear_on_submit=True):
        st.header("Contactemos")
        col1 ,col2 = st.columns(2)
        with col1:
            nombre= st.text_input("nombre")
        with col2:
            email= st.text_input("email")
        Descripcion = st.text_area("Descripcion")    
        btn_enviar = st.form_submit_button("Cargar")

    if btn_enviar:
        st.toast(f"Datos: {nombre}, Correo: {email}")
        st.success(f"Datos: {nombre}, Correo:{email}\n{Descripcion}")
