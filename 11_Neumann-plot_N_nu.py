import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc
import matplotlib          as mpl

mpl.rc('figure',  figsize=(13, 7))
mpl.rc('xtick', labelsize=21) 
mpl.rc('ytick', labelsize=21) 

x = np.linspace(0,50,1000)
J0 = sc.yv(0,x)
J1 = sc.yv(1,x)
J2 = sc.yv(2,x)
J3 = sc.yv(3,x)
J4 = sc.yv(4,x)

fig, ax = plt.subplots(layout="constrained")

ax.set_ylabel(r'$N_\nu(x)$',fontsize=21)
ax.set_xlabel(r'$x$',fontsize=23)
#ax.set_title('Funciones de Bessel de primer tipi',fontsize=12)

ax.set_ylim(-1.51,0.61)
#ax.plot(x,J0,x,J1,x,J2,x,J3,x,J4)
ax.plot(x,J0,color="black",lw=1.5) 
ax.plot(x,J1,color="red",lw=1.5)
ax.plot(x,J2,color="green",lw=1.5)
ax.plot(x,J3,color="blue",lw=1.5)
ax.plot(x,J4,color="orange",lw=1.5)

ax.legend((r'$N_0(x)$',r'$N_1(x)$',r'$N_2(x)$',r'$N_3(x)$',r'$N_4(x)$'),
          shadow=True, loc="lower right", handlelength=1.5, fontsize=22)
          
ax.grid()

plt.savefig("../Figuras/4.4_BesselGraph_2ndKind_N0-N4.png",dpi=400)

plt.show()