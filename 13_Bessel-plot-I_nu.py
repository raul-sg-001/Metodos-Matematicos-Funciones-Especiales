import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc
import matplotlib          as mpl

mpl.rc('figure',  figsize=(14, 10))
mpl.rc('xtick', labelsize=21) 
mpl.rc('ytick', labelsize=21) 

fig, ax = plt.subplots(2,layout="constrained",sharex=True)


################################################
## Gráfica de las funciones de Bessel modificadas de primer tipo
x = np.linspace(0,50,1000)
J0 = sc.iv(0,x)
J1 = sc.iv(1,x)
J2 = sc.iv(2,x)
J3 = sc.iv(3,x)
J4 = sc.iv(4,x)

ax[0].set_ylabel(r'$I_\nu(x)$',fontsize=21)
ax[0].set_xlabel(r'$x$',fontsize=23)

ax[0].set_ylim(-1,160)
ax[0].set_xlim(-0.1,10.1)

ax[0].plot(x,J0,color="black",lw=1.5) 
ax[0].plot(x,J1,color="red",lw=1.5)
ax[0].plot(x,J2,color="green",lw=1.5)
ax[0].plot(x,J3,color="blue",lw=1.5)
ax[0].plot(x,J4,color="orange",lw=1.5)

ax[0].legend((r'$I_0(x)$',r'$I_1(x)$',r'$I_2(x)$',r'$I_3(x)$',r'$I_4(x)$'),
          shadow=True, loc="upper right", handlelength=1.5, fontsize=22)
          
ax[0].grid()
################################################


################################################
## Gráfica de las funciones de Bessel modificadas de segundo tipo
J0 = sc.kv(0,x)
J1 = sc.kv(1,x)
J2 = sc.kv(2,x)
J3 = sc.kv(3,x)
J4 = sc.kv(4,x)

ax[1].set_ylabel(r'$K_\nu(x)$',fontsize=21)
ax[1].set_xlabel(r'$x$',fontsize=23)

ax[1].set_ylim(-0.01,1.0)
ax[1].set_xlim(-0.1,10.1)

ax[1].plot(x,J0,color="black",lw=1.5) 
ax[1].plot(x,J1,color="red",lw=1.5)
ax[1].plot(x,J2,color="green",lw=1.5)
ax[1].plot(x,J3,color="blue",lw=1.5)
ax[1].plot(x,J4,color="orange",lw=1.5)

ax[1].legend((r'$K_0(x)$',r'$K_1(x)$',r'$K_2(x)$',r'$K_3(x)$',r'$K_4(x)$'),
          shadow=True, loc="upper right", handlelength=1.5, fontsize=22)
          
ax[1].grid()
################################################

ax[0].text(0.015,0.20,"(a)",transform=ax[0].transAxes,fontsize=35,color="black",verticalalignment='top')
ax[1].text(0.015,0.20,"(b)",transform=ax[1].transAxes,fontsize=35,color="black",verticalalignment='top')


## Guardamos la figura
plt.savefig("../Figuras/4.6_BesselGraphs_I0-I4_K0-K4.png",dpi=400)

plt.show()




