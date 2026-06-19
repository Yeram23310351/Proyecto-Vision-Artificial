# Proyecto-Vision-Artificial
Aplicación de los conceptos de Visión Artificial mediante el entrenamiento de un modelo de la familia YOLO (You Only Look Once) para el reconocimiento de un conjunto de imágenes específico.
# Proyecto: Sistema de Inspección de Calidad Automatizado mediante Visión Artificial (YOLO)

### Integrante:
* JOSE RAMON NAVARRO MARQUEZ

---

## 1. Caso de Estudio: Clasificación de Fruta y Control de Calidad Agroindustrial

### A. Problema a Resolver
En las plantas empacadoras y distribuidoras de fruta, la presencia de piezas dañadas, podridas o mordidas por fauna/plagas merma la calidad del lote entero y acelera la descomposición de los productos sanos a su alrededor. La selección manual es lenta y poco higiénica. Este proyecto propone automatizar la inspección de calidad de manzanas en tiempo real en una línea de selección, identificando si una manzana está en estado óptimo o si se encuentra mordida/dañada utilizando el modelo YOLOv8.

### B. Hardware Propuesto (Entorno Industrial)
* **Cámara de Visión Industrial:** Una cámara Basler montada a una distancia focal fija sobre la banda transportadora para capturar imágenes de alta resolución de las manzanas en movimiento.
* **Sistema de Iluminación:** Iluminación domo LED de luz blanca fría difusa para evitar los brillos que produce la cáscara de la manzana y obtener colores reales.
* **Procesador de Borde (Edge Computing):** Una unidad Nvidia Jetson que recibe el flujo de video en tiempo real y ejecuta las inferencias del modelo YOLOv8 Nano en milisegundos.
* **Actuador de Separación:** Un brazo expulsor neumático o un soplador de aire comprimido industrial de alta presión controlado por una electroválvula de 24VCC.
* **Controlador Principal:** Un PLC Siemens S7-1200 encargado de recibir la señal de descarte y coordinar el actuador según la velocidad de la banda transportadora.

### C. Flujo de Funcionamiento
1. Las manzanas avanzan en fila sobre una banda transportadora de rodillos (los cuales hacen girar la fruta para que la cámara inspeccione todos sus lados).
2. La cámara captura continuamente el paso de cada pieza bajo la zona de iluminación.
3. El procesador Nvidia Jetson ejecuta el modelo YOLOv8 sobre cada cuadro de video para buscar dos clases específicas: `Manzana_Sana` o `Manzana_Mordida`.
4. Si el modelo detecta una manzana con la etiqueta `Manzana_Mordida` con una certeza mayor al 80%, envía inmediatamente una señal digital de alerta hacia el PLC.
5. El PLC calcula el tiempo exacto que tarda esa manzana en llegar al final de la banda y activa el actuador neumático, desviando la manzana dañada hacia una sección de merma o procesamiento secundario (como jugos), permitiendo que solo las manzanas perfectas continúen hacia el área de empaque final.

---

## Instrucciones de Ejecución

1. Instalar las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
