import streamlit as st
import cx_Oracle
import pandas as pd
from streamlit_option_menu import option_menu

st.title("LiBanco")
st.markdown("Aplicación de operaciones para sucursales y préstamos")

dsn = cx_Oracle.makedsn("c2", "1521", "XE")
connection = cx_Oracle.connect("system", "admin", dsn=dsn)
cursor = connection.cursor()


with st.sidebar:
    selected = option_menu("Menú", ["Sucursal", 'Préstamo', 'Ver tablas'], 
        icons=['signpost-split', 'cash-stack', 'inboxes'], menu_icon="cast", default_index=0)

def show_form1():
    opciones = ["Agregar", "Eliminar", "Actualizar"]

    # Crea los botones de radio
    eleccion = st.radio("Elige una opción", opciones)
    if eleccion == "Agregar":
        with st.form('form'):
            idsucursal = st.text_input("Id Sucursal")
            nombresucursal = st.text_input("Nombre de Sucursal")
            ciudadsucursal = st.text_input("Ciudad Sucursal")
            activos = st.number_input("Activos")
            region = st.number_input("Región")
            if st.form_submit_button(label='Agregar'):
                st.balloons();
                cursor.callproc('INSERT_SUCURSAL',[idsucursal, nombresucursal,ciudadsucursal,activos,region])
                cursor.execute("COMMIT")
    elif eleccion == "Eliminar":
        with st.form('form'):
            idsucursal = st.text_input("Id Sucursal")
            if st.form_submit_button('Eliminar'):
                cursor.callproc('DELETE_SUCURSAL',[idsucursal])
                cursor.execute("COMMIT")
                st.balloons();
    else:
        with st.form('form'):
            idsucursal = st.text_input("Id Sucursal")
            nombresucursal = st.text_input("Nombre de Sucursal")
            activos = st.number_input("Activos")
            if st.form_submit_button('Actualizar'):
                cursor.callproc('ACTUALIZAR_SUCURSAL',[idsucursal, nombresucursal,activos])
                cursor.execute("COMMIT")
                st.balloons();    
    

# Función que muestra el formulario 2
def show_form2():
    opciones = ["Agregar", "Eliminar", "Actualizar"]

    # Crea los botones de radio
    eleccion = st.radio("Elige una opción", opciones)
    if eleccion == "Agregar":
    # Muestra la opción elegida
        with st.form('form'):
            idsucursal = st.text_input("Id Sucursal")
            noprestamo = st.text_input("Número de Préstamo")
            cantidad = st.number_input("Cantidad")
            if st.form_submit_button('Agregar'):
                cursor.callproc('INSERT_PRESTAMO',[noprestamo, idsucursal, cantidad])
                st.balloons();
    elif eleccion == "Eliminar":
        with st.form('form'):
            noprestamo = st.text_input("Número de préstamo")
            if st.form_submit_button('Eliminar'):
                cursor.callproc('DELETE_PRESTAMO',[noprestamo])
                st.balloons();
    else:
        with st.form('form'):
            idsucursal = st.text_input("Id Sucursal")
            noprestamo = st.text_input("Número de Préstamo")
            cantidad = st.number_input("Cantidad")
            if st.form_submit_button('Actualizar'):
                cursor.callproc('ACTUALIZAR_PRESTAMO', [noprestamo, idsucursal, cantidad])
                st.balloons();

def show_tables():
    # Execute a SQL query
    cursor.execute("SELECT * FROM SUCURSAL")

    # Fetch results
    results = cursor.fetchall()

    # Create a DataFrame from the results
    df = pd.DataFrame(results, columns=[col[0] for col in cursor.description])

    st.subheader("SUCURSAL")
    st.write(df)

    cursor.execute("SELECT * FROM PRESTAMO")

    # Fetch results
    results = cursor.fetchall()

    # Create a DataFrame from the results
    df = pd.DataFrame(results, columns=[col[0] for col in cursor.description])

    st.subheader("PRESTAMO")
    st.write(df)
    
    cursor.execute("SELECT * FROM vista_cantidad_total_por_sucursal")

    # Fetch results
    results = cursor.fetchall()

    # Create a DataFrame from the results
    df = pd.DataFrame(results, columns=[col[0] for col in cursor.description])

    st.subheader("Cantidad de préstamos por sucursal")
    st.write(df)
    # Close cursor and connection
    cursor.close()
    connection.close()
    st.balloons(); 

col1, col2, col3 = st.columns(3)


if selected == 'Sucursal':
    show_form1()
    # with st.form('form'):
    #     idsucursal = st.text_input("Id Sucursal")
    #     nombresucursal = st.text_input("Nombre de Sucursal")
    #     ciudadsucursal = st.text_input("Ciudad Sucursal")
    #     activos = st.number_input("Activos")
    #     region = st.number_input("Región")
    #     if st.form_submit_button(label='Agregar'):
    #         st.balloons();
    #         cursor.callproc('INSERT_SUCURSAL',[idsucursal, nombresucursal,ciudadsucursal,activos,region])
    #         cursor.execute("COMMIT")
            #print("EXEC INSERT_SUC
elif selected == 'Préstamo':
    show_form2()
if selected == 'Ver tablas':
    show_tables();
    

st.markdown("""
    <style>
    div.stButton button:first-child {
        background-color: #F63366 !important;
        color: #FFFFFF !important;
    }
    div.stButton button:hover {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-family: sans-serif;
    }
    div.stButton button:checked {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-family: sans-serif;
    }
    </style>
""", unsafe_allow_html=True)