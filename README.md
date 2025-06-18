# registro-ventas-vendedores
Sistema en Python para registrar ventas y calcular comisiones

# 🧾 Sistema de Registro de Ventas para Vendedores Autónomos

Este proyecto está diseñado para ayudar a vendedores independientes a llevar un control eficiente y ordenado de sus ventas y comisiones, guardadas automáticamente en archivos de Excel.

---

## 🚀 ¿Qué hace este sistema?

- Permite **registrar ventas** indicando:
  - Nombre del vendedor
  - Producto vendido
  - Cantidad
  - Precio unitario
  - Porcentaje de comisión
- Calcula automáticamente:
  - **Total de la venta**
  - **Comisión correspondiente**
- Guarda toda la información en un archivo `.xlsx` (Excel) individual por vendedor.
- Incluye un **resumen automático al final del Excel** con el total acumulado de ventas y comisiones.
- Permite abrir el archivo del vendedor para consultar su historial desde el menú del sistema (solo en Windows).

---

## 🛠️ Tecnologías utilizadas

- Python 3
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

---

## ▶️ Cómo ejecutar el programa

1. Asegúrate de tener Python 3 instalado.
2. Instala las librerías necesarias:
   ```bash
   pip install pandas openpyxl
