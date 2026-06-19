# Proyecto-Vision-Artificial
Aplicación de los conceptos de Visión Artificial mediante el entrenamiento de un modelo de la familia YOLO (You Only Look Once) para el reconocimiento de un conjunto de imágenes específico.

# Proyecto: Sistema de Visión para Cosecha Automatizada y Estimación de Rendimiento Agrícola (YOLO)

### Integrantes:
* 23310351 CRISTIAN YERAM GONZALEZ MIRANDA
* 23310348 JOSE EDUARDO MARTINEZ DURAN

---

## 1. Caso de Estudio: Automatización de Cosecha y Monitoreo en Huertos

### A. Problema a Resolver
En el sector agrícola, la recolección manual de manzanas es una labor que requiere una gran cantidad de mano de obra y tiempo. Además, estimar el rendimiento de la cosecha observando los árboles de forma tradicional es impreciso. Este proyecto propone un sistema de visión artificial capaz de detectar manzanas en su entorno natural (directamente en las ramas del árbol o en superficies de recolección) utilizando el modelo YOLOv8. Esta detección es el paso fundamental para guiar vehículos agrícolas autónomos (Rovers) y brazos robóticos recolectores.

### B. Hardware Propuesto (Entorno Industrial-Agrícola)
* **Cámara de Visión Robótica:** Una cámara estéreo o RGB de amplio campo de visión (FOV) montada en el mástil de un vehículo agrícola autónomo.
* **Sistema de Iluminación:** Aprovechamiento de luz natural con filtros polarizadores para reducir el brillo de las hojas, complementado con focos LED estroboscópicos para compensar las sombras densas dentro del follaje del árbol.
* **Procesador de Borde (Edge Computing):** Una unidad Nvidia Jetson a bordo del vehículo que recibe el flujo de video en tiempo real y ejecuta las inferencias del modelo YOLOv8 Nano en milisegundos, ideal para robótica móvil.
* **Actuador de Recolección:** Un brazo robótico de múltiples grados de libertad equipado con un efector final de agarre suave (soft gripper) diseñado para no magullar la fruta.
* **Controlador Principal:** Un microcontrolador industrial o PLC compacto encargado de recibir las coordenadas de las manzanas detectadas en la imagen y traducirlas en cinemática inversa para mover el brazo robótico.

### C. Flujo de Funcionamiento
1. El vehículo autónomo avanza a velocidad constante por los pasillos del huerto de manzanas.
2. La cámara principal escanea continuamente el follaje de los árboles o las superficies de recolección.
3. El procesador Nvidia Jetson ejecuta el modelo YOLOv8 sobre cada cuadro de video, buscando e identificando las manzanas presentes en la escena.
4. Al detectar una manzana con un alto nivel de confianza, el sistema calcula la posición relativa (Bounding Box) del objeto dentro del entorno de trabajo.
5. El procesador envía las coordenadas al PLC o controlador del brazo robótico, el cual despliega el efector final hacia la posición exacta para recolectar la manzana y depositarla en el contenedor del vehículo.

---

## 🚀 Instrucciones de Ejecución

1. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
