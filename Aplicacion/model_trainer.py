from statsmodels.tsa.arima.model import ARIMA

def train_model(df):
	
	# Establecer la fecha como índice y agregar datos semanalmente
	data.set_index('Creado el', inplace=True)
    # Transformación a ingresos semanales
    df_semanal = data['Valor neto'].resample('W').sum()
    
    # Ajuste del modelo ARIMA
    model = ARIMA(df_semanal, order=(1, 1, 1))
    model_fit = model.fit()
	# Predecir ingresos para la siguiente semana
	forecast = arima_model.forecast(steps=1)
	print("Predicción de ingresos para la próxima semana:", forecast)
    print("Modelo entrenado.")
    return model_fit