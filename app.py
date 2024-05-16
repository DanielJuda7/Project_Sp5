import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.read_csv('vehicles_us.csv')
def imprimirGrafico(titulo,tipo,args): 
    st.write(titulo)
    if tipo == 1:
        figura = px.histogram(df, x=args[0])

    if tipo == 2:
        figura = px.scatter(df, x=args[0],y=args[1])

    if tipo == 3:
        figura = px.pie(names=args[0].index, values=args[0].values,
             title='Modelos más populares', hole=0.3)

    st.plotly_chart(figura, use_container_width=True)
      
st.header('Crea un gráfico')
#Se crea el botón para gráfico de histograma
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    titulo='Creación un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches'
    imprimirGrafico(titulo,1,['odometer'])       
#Se crea el botón para gráfico de dispersión    
scat_button = st.button('Construir Diagrama de dispersión') # crear un botón
if scat_button: # al hacer clic en el botón
    titulo='Creación un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches'
    imprimirGrafico(titulo,2,['odometer','price'])
#Se crea el botón para gráfico de pastel
pie_button=st.checkbox('Construir diagrama de pastel')
if pie_button:
    titulo='Modelos más populares'
    frecuencia_modelos = df['model'].value_counts()
    modelos_populares = frecuencia_modelos.head(5)
    imprimirGrafico(titulo,3,[modelos_populares])

                
 


