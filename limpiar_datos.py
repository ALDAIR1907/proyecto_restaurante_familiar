import pandas as pd

# 1. Leer el archivo CSV que descargaste de Google Sheets
df = pd.read_csv("registro_diario.csv")

# 2. Renombrar las columnas para que sean fáciles de usar (sin tildes ni espacios)
# OJO: Revisa que los nombres coincidan con los de tu formulario
df = df.rename(columns={
    'Marca temporal': 'marca_temporal',
    '¿Qué fecha es hoy?': 'fecha',
    '¿Cuánto vendiste hoy en total? (S/)': 'ventas_dia',
    '¿Cuánto gastaste hoy? (S/)': 'gastos_dia',
    '¿Qué platos se vendieron más hoy?': 'platos_vendidos'
})

# 3. Convertir fecha a formato real y quitar duplicados (si mamá llenó dos veces el mismo día, deja el último)
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=True)
df = df.drop_duplicates(subset="fecha", keep="last")

# 4. Asegurar que ventas y gastos sean números (si hay un error de tipeo, lo vuelve 0)
df["ventas_dia"] = pd.to_numeric(df["ventas_dia"], errors="coerce").fillna(0)
df["gastos_dia"] = pd.to_numeric(df["gastos_dia"], errors="coerce").fillna(0)

# 5. Calcular la ganancia diaria (Ventas - Gastos)
df["ganancia_dia"] = df["ventas_dia"] - df["gastos_dia"]

# 6. Guardar el archivo limpio (Este es el que usarás en Power BI)
df.to_csv("registro_limpio.csv", index=False, encoding='utf-8-sig')
print("✅ ¡Datos limpios! Archivo 'registro_limpio.csv' creado con éxito.")