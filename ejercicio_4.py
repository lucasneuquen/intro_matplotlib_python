# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico
    fig=plt.figure()
    fig.set_size_inches(10,10)    #averigué cómo cambiar el tamaño del fig para que entre todo
    fig.suptitle('Matplotlib - ejercicio 4', fontsize='25')
    
    ax1=fig.add_subplot(2,2,1)
    ax2=fig.add_subplot(2,2,2)
    ax3=fig.add_subplot(2,2,3)
    ax4=fig.add_subplot(2,2,4)
     
    ax1.set_title('Gráfico 1')
    ax1.plot(x,y1,color='r',label='potencia cuadrada')
    ax1.set_ylabel('resultado')
    ax1.set_xlabel('base')
    ax1.legend()
    ax1.set_facecolor('orange')
    ax1.grid(ls='dashed')
    
    ax2.set_title('Gráfico 2')
    ax2.plot(x,y2,color='b',label='potencia cúbica')
    ax2.set_ylabel('resultado')
    ax2.set_xlabel('base')
    ax2.legend()
    ax2.set_facecolor('pink')
    ax2.grid(ls='dashdot')
    
    ax3.set_title('Gráfico 3')
    ax3.plot(x,y3,color='g',label='potencia cuarta')
    ax3.set_ylabel('resultado')
    ax3.set_xlabel('base')
    ax3.legend()
    ax3.set_facecolor('whitesmoke')
    ax3.grid()
    
    ax4.set_title('Gráfico 4')
    ax4.plot(x,y4,color='b',label='raiz cuadrada')
    ax4.set_ylabel('resultado')
    ax4.set_xlabel('base')
    ax4.legend()
    ax4.set_facecolor('yellow')
    ax4.grid(ls='solid')
    
    plt.show(block=True)
    print("terminamos")
