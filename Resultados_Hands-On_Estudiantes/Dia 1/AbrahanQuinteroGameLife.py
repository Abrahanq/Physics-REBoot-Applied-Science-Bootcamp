# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:36:30 2021

@author: Abrahan
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as animation

# Se define el tamano del grid 

DimenX = 20
DimenY = 20

# Inicializamos el array 2D, que sera la grid
Grid = np.zeros((DimenX, DimenY))

# Se fija el seed para asi garantizar reproductibilidad de los resultados usando la funcion random seed

# Decidimos aleatoriamente inicializar algunos de los puntos del grid como 'vivos' con la funcion np.ramdom.randint
idx = np.random.randint(DimenX, size=(int(DimenX*(DimenY)),150))
# a y b pueden ser cualquier numero pero se necesita un numero mminimo de celdas.
#asignamos a estas posiciones aleatorias del array grid[(X, Y)] EL VALOR DE 1
Grid[(idx[20], idx[40])] = 1 #Argumentos columna 0 y columna 1

plt.figure()
plt.imshow(Grid)

#Definir funcion logica celda
def region_local(array, i, j):
    region = []
    
    for p in [-1,0,1]:
        for q in [-1,0,1]:
            if p != 0 or q != 0:
                region.append(array[np.mod((i+p),20)][np.mod((j+q),20)])
    return region
#Definimos la funcion logica celda
print(region_local(Grid,0,3))

def logica_celda(array,i,j,valor):
    r = region_local(array,i,j) #r es el subarray correspondiente a la region que rodea a la celula
    N_vecinos = 0 #N es el numero total de vecinos vivos ya que los muertos son 0
    for k in range(0,8):
      N_vecinos = N_vecinos + r[k]
    if valor == 1 and N_vecinos >= 2 and N_vecinos <=3: #Si la celula esta viva (i,j) = 1 y  hay 2 o 3 vecinos vivos asignamos 1
        return 1

 #Si hay menos de 2 o mas de 3 vecinos vivos, asignamos 0
    if valor == 1 and N_vecinos < 2 and N_vecinos >3:
      return 0
 #Si la celula esta muerta (i,j) = 0 y hay 3 vecinos vivos asignamos 1
    if valor == 0 and N_vecinos ==3:
      return 1

    else:
        return 0
    
    
def Ciclo(Grid):
    Tamano_grid = Grid.shape[0]
    for i in range(Tamano_grid):
        for j in range(Tamano_grid):
            Grid[i][j] = logica_celda(Grid,i,j,Grid[i][j])
    return Grid    

from IPython.display import HTML, Image
def Animar(i):
    Ciclo(Grid)
    ax1.clear()
    ax1.imshow(Grid)
    plt.suptitle('Generación N. {}'.format(i))

fig = plt.figure()
ax1 = fig.add_subplot()
animacion = animation.FuncAnimation(fig, Animar, interval=200,frames= 300)

animacion.save('Juego_de_la_vida.gif', writer='pillow', fps=60)
Image(url='Juego_de_la_vida.gif')