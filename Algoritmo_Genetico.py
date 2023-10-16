#Discretización del modelo
import numpy as np
import math
import matplotlib.pyplot as plt

from matplotlib import cm

xmin=-0
xmax=10
ymin=0
ymax=10
deltaxy=0.1
xr=np.arange(xmin, xmax, deltaxy)
yr=np.arange(ymin, ymax, deltaxy)


#MALLA DE VALORES PARA EVALUAR AL FUNCIÓN

X = xr
Y = yr
X,Y = np.meshgrid(X,Y)

Z = (-1.0* X**(1/2)* np.sin(X)*Y**(1/2)*np.sin(Y) )

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surface = ( ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False) )
plt.show()


#Parámetros Generales:
Q=20                            # Tamaño de población
M=2                             # Número de parámetros
dm1=0.01                        # Intervalo de muestreo del parámetro 1
dm2=0.01                        # Intervalo de muestreo del parámetro 2
Pc=0.9                          # Probabilidad de cruza (Cte: 90%)
Pm=0.15                         # Probabilidad de mutación (Cte: 5%)
NGen=2000                       # Número de generaciones máximas
Tol=0.01                        # Tolerancia (c/R al error)


Gen=zeros(Q,M)            # Arreglo 2D para almacenar los "Q" modelos
IndGen=zeros(Q,M)         # Arreglo 2D para almacenar los índices de los modelos
phi=zeros(Q,1)            # Arreglo 1D para almacenar la evaluación de los modelos
phim=1000				   # Valor inicial del mínimo global (se actualizará solo)
phii=1000				   # Valor inicial de mínimo de c/generación (se actualizará solo)