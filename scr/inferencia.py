import os
import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

# 1. Cargar el modelo YOLOv8 pre-entrenado (o el archivo 'best.pt' si entrenaron uno propio)
# Usamos el modelo nano ('n') por ser ideal para procesamiento rápido en entornos industriales
print("Cargando modelo YOLOv8...")
model = YOLO('yolov8n.pt') 

# 2. Definir la ruta de la imagen o video de prueba (Carpeta de evidencias)
# Nota: Asegúrate de tener una imagen llamada 'prueba.jpg' en tu carpeta de evidencias
ruta_imagen = 'evidencias/prueba.jpg'

if not os.path.exists(ruta_imagen):
    print(f"⚠️ Error: No se encontró la imagen en '{ruta_imagen}'.")
    print("Por favor, guarda una imagen de prueba en esa ruta para ejecutar el script.")
else:
    print(f"Ejecutando inferencia en: {ruta_imagen}...")
    
    # 3. Realizar la predicción (Inferencia) con el modelo
    # 'conf=0.25' significa que mostrará detecciones con más del 25% de certeza
    resultados = model.predict(source=ruta_imagen, conf=0.25, save=False)

    # 4. Procesar y mostrar los resultados usando Matplotlib (Como lo viste en clase)
    for resultado in resultados:
        # Dibujar las cajitas de selección (bounding boxes) sobre la imagen original
        imagen_con_detecciones = resultado.plot()
        
        # Convertir el color de BGR (OpenCV) a RGB (Matplotlib) para que se vea bien
        imagen_rgb = cv2.cvtColor(imagen_con_detecciones, cv2.COLOR_BGR2RGB)
        
        # Representación gráfica del resultado
        plt.figure(figsize=(10, 6))
        plt.imshow(imagen_rgb)
        plt.title("Detección de Objetos en Tiempo Real - Sistema de Inspección")
        plt.axis('off') # Ocultar los ejes para que se vea más limpio
        plt.show()
        
        print("Inferencia completada con éxito. ¡Imagen desplegada!")
