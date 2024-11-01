def clean_data(data):
	# Convertir la columna de fecha a tipo datetime 
	data['Creado el'] = pd.to_datetime(data['Creado el'])
	
	# Visualizar las primeras filas
	data.head()

	# Información sobre las columnas y tipos de datos
	data.info()

	# Estadísticas descriptivas
	data.describe()
    # Aplicar TRM
    data['Valor neto'] *= 4000

    # Verificar y limpiar Código Episodio
    data.drop_duplicates(subset=['Código Episodio'], inplace=True)
	
	#Comprobar la cantidad de valores nulos por cada campo
	data.isnull().sum()

    # Limpiar valores nulos
    data['Centro de Responsabilidad'].fillna('Desconocido', inplace=True)

    # Eliminar otros valores nulos
    data.dropna(inplace=True)

    print("Datos limpios.")
    return data