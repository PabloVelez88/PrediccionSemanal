
def schedule_weekly_run():
    # Configuración de la ejecución semanal cada lunes a las 00:00
    schedule.every().monday.at("00:00").do(main.main)
    df_semanal.to_csv('ingresos_hospital.csv')  # Exportar datos históricos de ingresos
	forecast.to_csv('predicciones_ingresos.csv')  # Exportar predicciones semanales
    print("Programado para correr cada semana.")
    print(df_semanal)
	print(forecast)
    while True:
        schedule.run_pending()
        time.sleep(1)