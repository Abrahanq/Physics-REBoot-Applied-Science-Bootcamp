# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 09:53:37 2021

@author: Abrahan
"""

"""
Modelo Seir tarea dia 1
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

"""Definimos las nuevas constantes
Tasa de infeccion, recuperacion, mortalidad
natalidad e incubacion """

# Tambien definimos las condiciones iniciales:
    
N0 = 1500 #Poblacion inicial
I0 = 1 #Poblacion inicial infectada
R0 = 0 #Poblacion incial recuperada
E0 = 0 #Poblacion incial expuesta
S0 = N0 - E0 - I0 - R0 #Poblacion inicial susceptible
 
# Constantes 
beta = 5 #Tasa de infeccion
gamma = 1./4 #Tasa de recuperacion
miu = 0.2 #Tasa de mortalidad
ni = 0.1 #Tasa de natalidad
alfa = 10 #Tasa de incubacion

Inicio = 0
Total_dias = 160
Num = 320
t = np.linspace(Inicio,Total_dias, Num)

# Definimos la funcion 
def Yt(y, t, beta, gamma, miu, ni, alfa, N):
    S, E, I, R = y
    N = S + E + I + R
    dSdt = -(beta * S * I) + (ni * N) - (miu * S)
    dEdt = (beta * S * I) - (alfa * E) - (miu * E)
    dIdt =  alfa * E - gamma * I - miu * I
    dRdt = gamma * I - miu * R
    return [dSdt/N, dEdt/N, dIdt/N, dRdt/N] 

Y0 = [S0, E0, I0, R0] #Condiciones iniciales

# Integracion de las ecuaciones SEIR en funcion de f
Sol = odeint(Yt, Y0, t, args=(beta, gamma, miu, ni, alfa, N0))
S, E, I, R = Sol.T


# Plot de los 5 grupos en curvas separadas
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)

ax.plot(t, S/1000, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, E/1000, 'g', alpha=0.5, lw=2, label='Exposed')
ax.plot(t, I/1000, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/1000, 'm', alpha=0.5, lw=2, label='Recovered with immunity')
ax.plot(t, (S+E+I+R)/1000, 'k', alpha=0.5, lw=2, label='Population')

ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0,1.2)

ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')

legend = ax.legend()
legend.get_frame().set_alpha(0.5)

for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
    
plt.show()