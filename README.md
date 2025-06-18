🐾 Proyecto Mini-AlexNet con Streamlit
Clasificación de imágenes en gato, perro o animal salvaje usando un modelo CNN inspirado en AlexNet y una aplicación web con Streamlit.

📁 Estructura del Proyecto
bash


1
2
3
4
5
6
7
animal_faces_project/
├── data/               # (No se sube al repo, ~1GB+)  
│   └── afhq/           # Dataset AFHQ (descargar desde Kaggle)  
├── models/             # (No se sube al repo)  
│   └── mini_alexnet_model.h5  # Modelo entrenado  
├── app.py              # Aplicación Streamlit  
└── train.py            # Entrenamiento del modelo  
🛠️ Requisitos
Python 3.8+
Librerías:
bash


1
pip install tensorflow streamlit numpy matplotlib scikit-learn
Dataset: Animal Faces (AFHQ) (descargar y organizar como se muestra en la estructura).
▶️ Uso
Entrenar el modelo :
bash


1
python train.py
Genera models/mini_alexnet_model.h5.
Ejecutar la aplicación :
bash


1
streamlit run app.py
📊 Métricas
Accuracy en validación
Matriz de confusión
Reporte de clasificación (precision, recall, f1-score)
⚠️ Notas
El dataset y el modelo guardado no se incluyen en el repositorio por su tamaño.
Asegúrate de tener GPU disponible para acelerar el entrenamiento.
Las imágenes deben estar en formato JPG/PNG y redimensionadas a 224x224 píxeles.
