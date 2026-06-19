import cv2
import os
from ultralytics import YOLO

def ejecutar_inferencia():
    # 1. Cargar el modelo con los pesos descargados
    # Asegúrate de colocar el archivo 'best.pt' en la misma ruta o especificar dónde está
    model = YOLO("runs/detect/train/weights/best.pt") 

    # 2. Ruta de la imagen de prueba (reemplaza si tu archivo se llama diferente o está en otra carpeta)
    ruta_imagen = "prueba.jpg" 

    if not os.path.exists(ruta_imagen):
        print(f"Error: No se encontró el archivo {ruta_imagen} en la raíz del proyecto.")
        return

    # 3. Ejecutar la predicción
    print("Procesando imagen con YOLOv8...")
    results = model(ruta_imagen)

    # 4. Crear la carpeta de evidencias si no existe
    os.makedirs("evidencias", exist_ok=True)

    # 5. Dibujar los cuadros de detección (bounding boxes) y guardar el resultado
    for r in results:
        im_bgr = r.plot()  # Dibuja las cajas y etiquetas sobre la imagen
        ruta_resultado = os.path.join("evidencias", "resultado_prueba.jpg")
        cv2.imwrite(ruta_resultado, im_bgr)
        print(f"¡Éxito! Imagen resultante guardada en: {ruta_resultado}")

if __name__ == "__main__":
    ejecutar_inferencia()
