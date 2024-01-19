import matplotlib.pyplot as plt
import csv

#'TypeData.csv'

def Graficar(rute):

    nombres = []
    puntuacion = []
    visualizaciones = []
    calificacion = []

    with open('Data/' + rute + '.csv', newline='', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv) 
        for fila in lector_csv:
            nombres.append(fila[0])
            puntuacion.append(int(fila[1]))
            visualizaciones.append(int(fila[2]) if fila[2] else 0)
            calificacion.append(fila[3])

    plt.figure(figsize=(18, 10))
    plt.scatter(puntuacion, visualizaciones, c='b', marker='o', s=5, label='Puntuación vs Visualizaciones')

    for i, nombre in enumerate(nombres):
        plt.annotate(nombre, (puntuacion[i], visualizaciones[i]), fontsize=8)

    plt.xlim(20, 70)
    plt.ylim(20, 70)

    plt.plot([0, 90], [90, 0], 'r-')

    plt.xlabel('Puntuación')
    plt.ylabel('Volumen')
    plt.title('Gráfico de Puntuación vs Volumen')

    plt.legend(loc='upper right')

    plt.grid(True)
    plt.tight_layout()

    plt.savefig('Graficas/'+ rute +'.png')

Graficar("AutomatizacionData")