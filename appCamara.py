import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from PIL import Image
import requests
from io import BytesIO

# Cargar el modelo entrenado
#with open('modelo_optimizado_Grupo_1.pkl', 'rb') as file:
#    modelo = pickle.load(file)

# Obtener la imagen desde la URL
url = "https://www.amsac.pe/images/ImagenCelular.jpg"
response = requests.get(url)
image = Image.open(BytesIO(response.content))

# Definir la interfaz de usuario en Streamlit
st.title('Predicción de Precios de Celulares')
#agregar imagen
st.image(image)

# Controles de entrada para las características
ram = st.number_input('RAM (GB)', min_value=1, max_value=64, value=8)
almacenamiento = st.number_input('Almacenamiento (GB)', min_value=64, max_value=512, value=128)
tipoCelular_BusinessPhone = st.selectbox('¿Es Para Negocios?', ['No', 'Sí'])
tipoCelular_CameraPhone = st.selectbox('¿Es Para usarlo como Camara?', ['No', 'Sí'])
tipoCelular_GamingPhone = st.selectbox('¿Es para Gamer?', ['No', 'Sí'])
tipoCelular_Smartphone = st.selectbox('¿Es Smartphone?', ['No', 'Sí'])
marca_Samsumg = st.selectbox('Desea Marca Samsumg', ['No', 'Sí'])
marca_Xiaomi = st.selectbox('¿Desea Marca Xiaomi?', ['No', 'Sí'])
marca_iPhone = st.selectbox('¿Desea Marca iPhone?', ['No', 'Sí'])


# Convertir entradas a formato numérico
TipoCelular_BusinessPhone = 1 if type_gaming == 'Sí' else 0
tipoCelular_CameraPhone = 1 if type_notebook == 'Sí' else 0
tipoCelular_GamingPhone = 1 if type_gaming == 'Sí' else 0
tipoCelular_Smartphone = 1 if type_notebook == 'Sí' else 0
marca_Samsumg = 1 if type_gaming == 'Sí' else 0
marca_Xiaomi = 1 if type_notebook == 'Sí' else 0
marca_iPhone = 1 if type_gaming == 'Sí' else 0


 # Botón para realizar predicción
if st.button('Predecir Precio'):
    # Cargar el modelo entrenado
    with open('TrabajoFinal_Grupo1.pkl', 'rb') as file:
        modelo = pickle.load(file)   
    
    # Crear DataFrame con las entradas
    input_data = pd.DataFrame([[ram, almacenamiento, tipoCelular_BusinessPhone, tipoCelular_CameraPhone, tipoCelular_GamingPhone, tipoCelular_Smartphone, marca_Samsumg, marca_Xiaomi, marca_iPhone]],
                    columns=['Ram','Almacenamiento', 'TipoCelular_BusinessPhone', 'TipoCelular_CameraPhone', 'TipoCelular_GamingPhone', 'TipoCelular_Smartphone', 'Marca_Samsumg', 'Marca_Xiaomi', 'Marca_iPhone'])

    # Estandarización de las características
    scaler = StandardScaler()
    input_scaled = scaler.fit_transform(input_data)

    # Realizar predicción
    prediction = modelo.predict(input_scaled)

    # Mostrar predicción
    st.write(f'Precio de Celular predecido: {prediction[0]:.2f} Dolares')


