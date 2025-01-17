# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 16:07:34 2021

@author: Abrahan
"""

"""
Modelo SIR, tarea dia 1
"""
# importamos las librerias
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt 

# Definimos los parametros iniciales
N = 1500
I0, R0 = 1, 0
S0 = N - I0 - R0 
beta, gamma = 0.2, 1./10
# Usamos los mismos nombres que las variables y constantes que se necesitan

Total_dias = 160

Num = 320 # Dos puntos de datos por dia  
Inicio = 0 
# Inicializamos el array 1D
t = np.linspace(Inicio, Total_dias, Num)

# Definimos primero la funcion a resolver, la variable independiente y luego las constantes
def Y(y, t, beta, gamma):
    S, I, R = y[0], y[1], y[2]
    dSdt = - (beta * S * I)/N
    dIdt = (beta * S * I)/N - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

#Ahora hacemos un vector con las condiciones iniciales definidas al principio
Y0 = [S0, I0, R0]

Sol = odeint(Y, Y0, t, args=(beta, gamma))
[S, I, R] = Sol.T    
fig = plt.figure(facecolor='w')
#fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)

ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible') #Suceptible vs t
ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected') # Infectado vs t
ax.plot(t, R/1000, 'g', alpha=0.5, lw=2, label='Recovered with immunity') #Recuperado vs t

ax.set_xlabel('Time /days') #titulo del eje X
ax.set_ylabel('Number (1000s)') #titulo eje y
ax.set_ylim(0,1.2) #min z max del eje Y
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')

legend = ax.legend()
legend.get_frame().set_alpha(0.5)

for spine in ('top', 'right', 'bottom', 'left'): 
    ax.spines[spine].set_visible(False)
    
plt.show()




