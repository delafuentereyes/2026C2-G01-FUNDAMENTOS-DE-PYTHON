"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""
from sedes import sedes

# DEFINICIÓN DE FUNCIONES
def calcular_total(ventas):
    """Recibo una lista, la sumo y retorno el total"""
    return sum(ventas)

def calcular_promedio(lista): # EL NOMBRE DENTRO DEL () ES REPRESENTATIVO, CUANDO LA FUNCIÓN SE INVOCA SE COLOCAN LOS DATOS REALES
    """Retorna el promedio de ventas de una lista"""
    return sum(lista) / len(lista)

def calcular_porcentaje(total, meta, formato = False):
    porcentaje = total / meta * 100
    if formato:
        return f"{porcentaje:.2f}%"
    return porcentaje

def calcular_clasificacion(total, meta):
    porcentaje = calcular_porcentaje(total, meta) # SE PUEDE LLAMAR UNA FUNCIÓN DENTRO DE OTRA
    if porcentaje >= 100:
        mensaje_sede = 'Meta alcanzada'
    elif porcentaje >= 80:
        mensaje_sede = 'Meta CASI alcanzada. Prestar atención'
    else:
        mensaje_sede = 'Meta NO alcanzada. URGE atención'
    return mensaje_sede

def imprimir_reporte(lista):
    total_ventas = calcular_total(ventas)
    promedio = calcular_promedio(lista)
    porcentaje = calcular_porcentaje(total, meta)
    clasificacion = calcular_clasificacion(total, meta)
    
    print("-" * 15)
    print('REPORTE DE VENTAS')
    print("-" * 15)
    print("\n")
    
    print(f"Ventas totales por sede: ₡{total_ventas}")
    print(f"Promedio diario por sede: {promedio}%")
    print(f"Porcentaje de meta alcanzada por meta: {porcentaje}")
    print(f"Clasificación de la meta por sede: {clasificacion}")

#print("Cantidad de sedes:", len(sedes))
#print("Tipo de variable sedes:", type(sedes))
#print("Tipo de variable sedes [0]:", type(sedes[0]))
#print("Datos por sede:", sedes[0].keys()) # DEVUELVE LAS ETIQUETAS DE LA sedes[0]
#print("Primera sede:", sedes[0]) # DEVUELVE LOS DATOS DE LA sedes[0]
#print("Nombre de la primera sede:", sedes[0]['nombre']) # DEVUELVE UN VALOR EN CONCRETO DE LA sedes[0]

reporte = []
venta_mas_alta = 0

for sede in sedes:
    ventas = sede['ventas']
    meta = sede['meta']
    total_sede = calcular_total(ventas) # SE INVOCA LA FUNCIÓN Y SE LE PASAN LOS DATOS SOLICITADOS
    promedio_sede = calcular_promedio(ventas)
    porcentaje_sede = calcular_porcentaje(total_sede, meta, True)
    estado = calcular_clasificacion(total_sede, meta)
    
    print(total_sede, promedio_sede, porcentaje_sede)
    #if venta_mas_alta <= total_sede:
        #venta_mas_alta = total_sede
        # AGREGAR EN UNA LISTA LA SEDE
#print(imprimir_reporte(reporte))
# SEDE MÁS INGRESOS
# PROVINCIAS