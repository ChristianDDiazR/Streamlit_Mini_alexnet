# 🐾 Proyecto Mini-AlexNet con Streamlit

Clasificación de imágenes en **gato**, **perro** o **animal salvaje** utilizando un modelo de red neuronal convolucional (CNN) inspirado en AlexNet y una aplicación web desarrollada con **Streamlit**.

---

## 📁 Estructura del Proyecto

animal_faces_project/
├── data/ # (No se sube al repo, ~1GB+)
│ └── afhq/ # Dataset AFHQ (descargar desde Kaggle)
├── models/ # (No se sube al repo)
│ └── mini_alexnet_model.h5 # Modelo entrenado
├── app.py # Aplicación Streamlit
└── train.py # Script de entrenamiento
