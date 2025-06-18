""" tabla de vendedores """
import pandas as pd
import os
from datetime import datetime
import openpyxl

### Registro de ventas ###

def registrar_ventas():
    
    print("\n--- Resgistro de Nueva Venta ---")
    
    nombre_archivo = input("Nombre del archivo Excel(sin.xlsx):").strip()
    archivo = f"{nombre_archivo}.xlsx"
    
    ### Datos de Venta ###
    
    vendedor = input("Nombr del vendedor: ")
    producto = input("Nombre del producto: ")
    cantidad = int(input("Cantidad vendida:"))
    precio_unitario = float(input("Precio unitario del producto ($):"))
    comision_porcentaje = float(input("Comision (%) por producto:"))
    
    total_ventas = cantidad * precio_unitario
    comision_total = total_ventas * (comision_porcentaje / 100)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    nueva_venta = {
        "Fecha": fecha,
        "Vendedor": vendedor,
        "Producto": producto,
        "Cantidad": cantidad,
        "Precio_unitario": precio_unitario,
        "Total_ventas": round(total_ventas,2),
        "Comision": round(comision_total, 2) 
    }
    
    ### lectura o creacion del archivo excel ###
    
    if os.path.exists(archivo):
        df = pd.read_excel(archivo)

        # Eliminar filas previas de resumen si existen
        df = df[~df["Vendedor"].isin(["TOTAL VENTAS", "TOTAL COMISION"])]
        
        # Agregar la nueva fila
        df = pd.concat([df, pd.DataFrame([nueva_venta])], ignore_index=True)
    else:
        df = pd.DataFrame([nueva_venta])

    # Calcular totales acumulados
    total_ventas_sum = df["Total_ventas"].sum()
    total_comision_sum = df["Comision"].sum()
    
    ### Fila vacia para los totales ###
    
    fila_vacia = {col: "" for col in df.columns}

    fila_total_ventas = {
        "Fecha": "",
        "Vendedor": "TOTAL VENTAS",
        "Producto": "",
        "Cantidad": "",
        "Precio_unitario": "",
        "Total_ventas": round(total_ventas_sum, 2),
        "Comision": ""
    }

    fila_total_comision = {
        "Fecha": "",
        "Vendedor": "TOTAL COMISION",
        "Producto": "",
        "Cantidad": "",
        "Precio_unitario": "",
        "Total_ventas": "",
        "Comision": round(total_comision_sum, 2)
    }

    # Agregar filas de totales al final
    df = pd.concat([
        df,
        pd.DataFrame([fila_vacia]),
        pd.DataFrame([fila_total_ventas]),
        pd.DataFrame([fila_total_comision])
    ], ignore_index=True)

    # Guardar
    df.to_excel(archivo, index=False)
    print(f"✅ Venta registrada y totales actualizados en '{archivo}'")
    
    ### ajuste de columnas ###
    
    wb = openpyxl.load_workbook(archivo)
    ws = wb.active
    
    for column_cells in ws.columns:
        length = max(len(str(cell.value)) if cell.value is not None else 0 for cell in column_cells)
        ws.column_dimensions[column_cells[0].column_letter]. width = length + 2
    
    ### Menu principal ###
    
while True:
    print("\n1. Registrar nueva venta")
    print("2. Ver istorial de un vendedor")
    print("3. salir")
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        registrar_ventas()
    
    elif opcion == "2":
        vendedor = input("Nombre del vendedor").strip()
        archivo = f"{vendedor}.xlsx"
        if os.path.exists(archivo):
            os.startfile(archivo)
            print(f"✅ Archivo '{archivo}' abierto.")
        else:
            print(f"❌ No existe historial para el vendedor '{vendedor}'.")
    elif opcion == "3":
        print("👋 ¡Hasta luego!")
        break
    
    else:
        print("❌ Opción no válida. Intenta de nuevo.")
        
    