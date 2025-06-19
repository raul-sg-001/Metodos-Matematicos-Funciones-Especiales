import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc


T = np.linspace(0,1,10)

X = np.arange(0,1,0.001)
Y = np.arange(0,1,0.001)

X,Y = np.meshgrid(X,Y)

L = 1.0
c = 1.0


def f(n,x,y,t):
   kan    = (2*n +1)*np.pi/L
   omegan = kan*c
   y = (8*L*L*np.cos(omegan*t)*np.sin(kan*x))/(np.power(2*n+1,3)*np.power(np.pi,3))
   return(y)
   
Nterm = 200
t = 0.0
Z = f(0,X,Y,t)
for m in range(1,Nterm):
   Z += f(m,X,Y,t)


t = 0.3
Z1 = f(0,X,Y,t)
for m in range(1,Nterm):
   Z1 += f(m,X,Y,t)


t = 0.6
Z2 = f(0,X,Y,t)
for m in range(1,Nterm):
   Z2 += f(m,X,Y,t)



fig = plt.figure(layout="constrained",figsize = (12,6))
#ax = Axes3D(fig)
#ax = fig.gca(projection='3d')
ax =fig.add_subplot(projection='3d')
surface = ax.plot_surface(X,Y,Z, cmap = "coolwarm")
surface1 = ax.plot_surface(X,Y,Z1, cmap = "coolwarm")
surface2 = ax.plot_surface(X,Y,Z2, cmap = "coolwarm")
#fig.colorbar(surface)
#fig.colorbar(surface1)
#fig.colorbar(surface2)

ax.set_ylabel(r'$x$',fontsize=20)
ax.set_xlabel(r'$y$',fontsize=20)

ax.set_zlabel(r'$\psi(x,y,t)$',fontsize=20)



"""
t = 0.05
Z005= f(0,X,0,t)
for m in range(1,len(alp)):
   Z005 += f(m,X,0,t)

t = 0.1
Z01 = f(0,X,0,t)
for m in range(1,len(alp)):
   Z01 += f(m,X,0,t)


t = 0.1
Z001 = f(0,X,0,t)
for m in range(1,Nterm):
   Z001 += f(m,X,0,t)

t = 0.6
Z005 = f(0,X,0,t)
for m in range(1,Nterm):
   Z005 += f(m,X,0,t)

t = 1.20
Z01 = f(0,X,0,t)
for m in range(1,Nterm):
   Z01 += f(m,X,0,t)


t = 2.3
Z05 = f(0,X,0,t)
for m in range(1,Nterm):
   Z05 += f(m,X,0,t)


plt.plot(X,Z0001,"black")
plt.plot(X,Z005,"red")
plt.plot(X,Z01,"orange")
plt.plot(X,Z05,"blue")
"""


plt.show()




