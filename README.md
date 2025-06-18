# Clasificador de caras de animales con Mini-AlexNet y Streamlit

Este proyecto implementa un modelo CNN inspirado en AlexNet y una aplicación web con Streamlit que realiza la clasificación de imágenes en gato, perro o animal salvaje.

## Archivos del proyecto

Debido al tamaño de los archivos, solo se incluyen en este repositorio:

- `train.py`: Script para entrenar y guardar el modelo.
- `app.py`: Aplicación de Streamlit para cargar imágenes y mostrar predicciones.

## Enlaces importantes

- [Descargar dataset "Animal Faces"]([https://www.kaggle.com/competitions/leaf-classification/data](https://www.kaggle.com/datasets/andrewmvd/animal-faces))
- [Descargar modelo entrenado desde Google Drive]([https://drive.google.com/your-model-link](https://drive.google.com/drive/folders/1DtGI12GzraCLKuTkD13BbSGM_TEI5FkW?usp=sharing))

## Requisitos

Instala las dependencias necesarias con:

```bash
pip install tensorflow streamlit numpy matplotlib scikit-learn
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

```plaintext
Streamlit_Mini-AlexNet/
│
├── app.py
├── train.py
├── data/
│   └── afhp/
│      └── train/
│      │   └── (carpetas con fotos de perros, gatos y animales salvajes)
│      └── val/
│          └── (carpetas con fotos de perros, gatos y animales salvajes) 
│
├── models/
│   └── mini_alexnet.h5        # Modelo entrenado (descargable desde Drive)
