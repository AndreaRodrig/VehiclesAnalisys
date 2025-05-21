import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado principal
st.header('Visualización interactiva de anuncios de vehículos')

# Casilla para construir un histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write('Creando un histograma para la columna "odometer"')
    fig_hist = px.histogram(car_data, x="model", # Crear un histograma
        y="price", 
        color="condition", 
        title="Distribución de Precios por Modelo y Condición",
        barmode="stack") 
    st.plotly_chart(fig_hist, use_container_width=True)


# Casilla para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Creando un gráfico de dispersión: precio vs. odómetro')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color='cylinders',title="Precio vs. Kilometraje (coloreado por número de cilindros)")
    st.plotly_chart(fig_scatter, use_container_width=True)
