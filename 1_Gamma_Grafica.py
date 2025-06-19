import numpy               as np
import matplotlib.pyplot   as plt
import scipy.special       as sc
import matplotlib          as mpl

mpl.rc('figure',  figsize=(10, 6))
mpl.rc('xtick', labelsize=18) 
mpl.rc('ytick', labelsize=18) 

x = np.linspace(-5.5,5,100000)
Gamma = sc.gamma(x)

fig, ax = plt.subplots(layout="constrained")

ax.set_ylabel(r'$\Gamma(x)$',fontsize=20)
ax.set_xlabel(r'$x$',fontsize=18)
ax.set_title('Función gamma en variable real',fontsize=20)

ax.set_ylim(-25,25)
ax.set_xlim(-5,5)
ax.plot(x,Gamma,'black')
ax.plot(x,0*x,'--r')
ax.grid()

plt.savefig("../Figuras/originales/1_GraficaFuncionGamma.png",dpi=400)

plt.show()