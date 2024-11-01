import data_loader
import data_cleaner
import analysis
import model_trainer
import predictor
import scheduler

def main():
    # Cargar datos
    df = data_loader.load_data('./Facturacion.xlsx')
    
    # Limpiar datos
    df_clean = data_cleaner.clean_data(df)
    
    # Análisis exploratorio y pruebas estadísticas
    analysis.perform_exploratory_analysis(df_clean)
    
    # Entrenamiento del modelo
    model = model_trainer.train_model(df_clean)
    
    # Realizar predicción para la próxima semana
    prediction = predictor.make_prediction(model)
    print("Predicción para la próxima semana:", prediction)

    # Programar la ejecución automática semanal
    scheduler.schedule_weekly_run()

if __name__ == "__main__":
    main()