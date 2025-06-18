# Clasificador de caras de animales con Mini-AlexNet y Streamlit

Este proyecto implementa un modelo CNN inspirado en AlexNet y una aplicación web con Streamlit que realiza la clasificación de imágenes en gato, perro o animal salvaje.

## 📁 Archivos del proyecto

Debido al tamaño de los archivos, solo se incluyen en este repositorio:

- `train.py`: Script para entrenar y guardar el modelo.
- `app.py`: Aplicación de Streamlit para cargar imágenes y mostrar predicciones.

## 🔗 Enlaces importantes

- 📦 [Descargar dataset "Animal Faces"]([https://www.kaggle.com/competitions/leaf-classification/data](https://www.kaggle.com/datasets/andrewmvd/animal-faces))
- 💾 [Descargar modelo entrenado desde Google Drive]([https://drive.google.com/your-model-link](https://drive.google.com/drive/folders/1DtGI12GzraCLKuTkD13BbSGM_TEI5FkW?usp=sharing))

## ⚙️ Requisitos

Instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

Si se desea entrenar el modelo el comando es el siguiente

```bash
python train.py
```

Y luego para ejecutar la aplicación

```bash
streamlit run app.py
```

## Estructura del proyecto
El proyecto debe tener esta estructura:

Data
  afhq
    train
      (carpetas con fotos)
    val
      (carpetas con fotos)
Models
  mini_alexnet_model.h5
app.py
train.py
