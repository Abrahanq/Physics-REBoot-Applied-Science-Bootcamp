# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:27:50 2021
El juego de la vida
@author: Abrahan
"""

import math 
import numpy as np 
from scipy.integrate import  odeint 
from matplotlib import pyplot as plt


# Se define la ecuacion de movimiento del pendulo
    
g = 9.8  # [m/s^2] 
largo = 10 #[m]
masa = 1 #[Kg]
inicio = 0
Total_s = 10
Num = 300
t = np.linspace(inicio, Total_s, Num)

def f(X, t, g, largo ,masa):
    theta = X[0] #Posicion angular
    omega = X[1] #Velocidad angular

    return np.array([omega, -(masa*g*math.sin(theta)/largo)]) #(derivada de X[0], derivada de X[1]), (Velocidad Angular, Aceleracion)

# Condiciones Iniciales como un array
X0 = [np.pi/2, 0] 
Sol = odeint(f, X0, t, args=(g,largo,masa)) 

[theta, omega] = Sol.T

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax1.plot(t, theta) #Entrada 0 del vector X
ax1.set_ylabel('Posición Angular',fontweight='bold')
ax1.set_xlabel('Tiempo (s)',fontweight='bold')
ax1.grid()
ax2 = fig.add_subplot(1,2,2)
ax2.plot(t, omega) #Entrada 1 del vector X
ax2.set_ylabel('Velocidad Angular', fontweight='bold')
ax2.set_xlabel('Tiempo (s)',fontweight='bold')
ax2.grid()
plt.tight_layout()