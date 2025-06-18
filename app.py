import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

@st.cache_resource
def load_model():
    return tf.keras.models.load_model('models/mini_alexnet_model.h5')

model = load_model()

def predict(image):
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    class_names = ['Cat', 'Dog', 'Wild']
    return class_names[np.argmax(prediction)], np.max(prediction)

st.title("Clasificador de Caras de Animales")
st.write("Sube una imagen para clasificar si es un gato, perro o animal salvaje.")

uploaded_file = st.file_uploader("Elige una imagen...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Imagen cargada", use_column_width=True)
    label, confidence = predict(image)
    st.write(f"**Predicción:** {label}")
    st.write(f"**Confianza:** {confidence:.2%}")
