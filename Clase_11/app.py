"""Programa principal del proyecto modular BCCR"""

import matplotlib.pyplot as plt

from lectura_datos import URL_BCCR, cargar_tabla_bccr
from limpieza_datos import limpiar_datos, filtrar_diferencial_alto, filtrar_por_tipo_entidad

def mostrar_primeras_entidades(data):
    """Muestra una vista de las columnas principales"""
    columnas = ['ENTIDAD', 'COMPRA', 'VENTA', 'DIFERENCIAL']
    print(data[columnas].head().to_string(index=False))
    
def ejecutar():
    datos_crudos = cargar_tabla_bccr(URL_BCCR)
    datos = limpiar_datos(datos_crudos)
    print('Datos cargados exitosamente de https://gee.bccr.fi.cr/')
    while True:
        print('\n', '*' * 30,'PROYECTO DE ANÁLISIS BCCR', '*' * 30)
        print('1. Mostrar primeras entidades limpias')
        print('2. Mostrar entidades con diferencial superior al promedio')
        print('3. Promedio por tipo entidad')
        print('4. Mostrar lista de entidades')
        print('5. Graficar')
        print('6. Salir')
        
        opcion = input('---> Ingrese la opción del menú: ').lower().strip()
        
        if opcion == '1':
            mostrar_primeras_entidades(datos)
        elif opcion == '2':
            resultado = filtrar_diferencial_alto(datos)
            resultado = resultado.sort_values(by='DIFERENCIAL', ascending=False)
            mostrar_primeras_entidades(resultado)
        elif opcion == '3':
            filtrado = filtrar_por_tipo_entidad(datos)
            print('\n', filtrado.to_string())
        elif opcion == '4':
            pass
        elif opcion == '5':
            alertas = filtrar_diferencial_alto(datos)
            if alertas.empty:
                print("No hay datos para graficar.")
                return
            
            top_cinco = alertas.sort_values("DIFERENCIAL", ascending=False).head(5)
            top_cinco = top_cinco.sort_values("DIFERENCIAL")
            
            grafico = top_cinco.plot(
                kind="barh",
                x="ENTIDAD",
                y="DIFERENCIAL",
                legend=False,
                color="steelblue",
                title="Entidades con mayor diferencial",
            )
            grafico.set_xlabel("Diferencial (VENTA - COMPRA)")
            grafico.set_ylabel("Entidad autorizada")
            plt.tight_layout()
            plt.show()
        elif opcion == '6':
            print("\nAnálisis finalizado")
            input("Presione tecla 'ENTER' para salir...\n")
            break
        else:
            print('ERROR ---> Opción inválida.\nEscriba un número del 1 al 6.')
        input("\nPresione tecla 'ENTER' para continuar...\n")

if __name__ == "__main__":
    ejecutar()