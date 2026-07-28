"""Funciones para limpiar y filtrar los datos cambiarios."""

import pandas as pd


def limpiar_datos(datos):
    """Prepara la tabla del BCCR y calcula la columna Diferencial."""
    datos_limpios = datos.copy()

    datos_limpios.columns = datos_limpios.iloc[0]
    datos_limpios = datos_limpios.iloc[1:].reset_index(drop=True)
    datos_limpios["Tipo de Entidad"] = (
        datos_limpios["Tipo de Entidad"].ffill()
    )
    datos_limpios = datos_limpios.dropna(
        subset=["Entidad Autorizada"]
    ).copy()

    columnas_numericas = ["Compra", "Venta"]

    if "Diferencial Cambiario" in datos_limpios.columns:
        columnas_numericas.append("Diferencial Cambiario")

    for columna in columnas_numericas:
        datos_limpios[columna] = pd.to_numeric(
            datos_limpios[columna],
            errors="coerce",
        )

    datos_limpios = datos_limpios.dropna(
        subset=["Compra", "Venta"]
    ).copy()
    datos_limpios["Diferencial"] = (
        datos_limpios["Venta"] - datos_limpios["Compra"]
    )

    #Renombrar nombres Columnas
    datos_limpios.rename(columns = {
        'Tipo de Entidad':'TIPO',
        'Entidad Autorizada': 'ENTIDAD',
        'Diferencial Cambiario': 'DIFERENCIAL',
        'Compra':'COMPRA',
        'Venta': 'VENTA',
        'Última Actualización':'FECHA'
    }, inplace=True)
    return datos_limpios

def filtrar_diferencial_alto(data: pd.DataFrame) -> pd.DataFrame:
    """Devuelve diferenciales altos en un DF"""
    promedio_diferencial = data['DIFERENCIAL'].mean()
    filro = data['DIFERENCIAL'] > promedio_diferencial
    return data[filro].copy()

def filtrar_por_tipo_entidad(data: pd.DataFrame):
    """Agrupar por tipo de entidad y calcular el promedio de compra, venta y diferencial"""
    columnas = ['COMPRA', 'VENTA', 'DIFERENCIAL']
    data_agrupada = (
        data.groupby('TIPO')[columnas]
        .mean()
        .round(2)
        .sort_values(by='DIFERENCIAL', ascending=False)
    ).copy()
    return data_agrupada