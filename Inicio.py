import streamlit as st

def inicio ():
    st.title("Inicio")
    st.markdown("## Proyecto de prueba de carga")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### prub 1 ")
    with col2:
        st.markdown("### columna 2")
    with col3:
        st.markdown("### prub 3")

    st.divider()