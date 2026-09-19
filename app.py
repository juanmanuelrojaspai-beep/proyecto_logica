import streamlit as st 
from Inicio import inicio
from Formulario import formulario 
from tabla import tabla 

st.set_page_config(page_title="proyecto", layout="wide")

def main():
    menu = ["inicio","formulario","tabla"]
    choice = st.sidebar.selectbox("menu", menu)

    if choice == "inicio":
        inicio()
    elif choice == "formulario":
        formulario()
    elif choice =="tabla":
        tabla()

if __name__== "__main__":
    main()