import streamlit as st 
import pandas as pd 

def crearTabla(num1,num2):
    valor1= int(num1)
    valor2= int(num2)
    resultado = valor1*valor2

    datos = [{"numero1":valor1,"numero2":valor2,"resultado":resultado}]

    df_tabla = pd.DataFrame(datos)
    return df_tabla



def tabla():
    with st.form("tablas", clear_on_submit=True):

        st.title('Formulario Tablas')
        num1 = st.number_input("Numero 1" , step=1)
        num2 = st.number_input("Numero 2" , step=1)
        btn_enviar= st.form_submit_button("Evaluar")
    if btn_enviar:
        if num1 and num2:    
            st.spinner("cargando . . . ")
            st.dataframe(crearTabla(num1,num2))
