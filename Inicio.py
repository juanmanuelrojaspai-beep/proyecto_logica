import streamlit as st

def inicio ():
    st.title("Inicio")
    st.markdown("## Proyecto Matematicas")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### operador logico and  ")
    with col2:
        st.markdown("### operador logico or")
    with col3:
        st.markdown("### operador logico not")

    st.divider()
