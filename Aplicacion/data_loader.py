
import pandas as pd

def load_data(filepath):
    try:
        data = pd.read_excel(filepath)
        print("Datos cargados exitosamente.")
        return data
    except Exception as e:
        print("Error al cargar los datos:", e)
        return None