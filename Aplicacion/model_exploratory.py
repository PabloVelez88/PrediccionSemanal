import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import scipy.stats as stats

def perform_exploratory_analysis(data):
    # Histogramas para las variables numéricas
	data.hist(bins=15, figsize=(10, 2))
	plt.show()

	# Boxplot para detectar outliers
	sns.boxplot(x=data['Valor neto'])
	plt.show()
	
	# Gráficos de barras para variables categóricas
	for col in ['Aseguradora','Clase episodio','Población']:
		plt.figure(figsize=(15, 2))
		sns.countplot(data=data, x=col)
		plt.title(f'Conteo de {col}')
		plt.show()
		
    # Matriz de correlación
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
    plt.title("Matriz de Correlación")
    plt.show()

    # Autocorrelación
    df_semanal = data['Valor neto'].resample('W').sum()
    plot_acf(df_semanal)
    plt.show()
    plot_pacf(df_semanal)
    plt.show()
