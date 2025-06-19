import numpy               as np
import matplotlib.pyplot   as plt
import scipy.special       as sc
import matplotlib          as mpl

mpl.rc('figure',  figsize=(12, 7))
mpl.rc('xtick', labelsize=18) 
mpl.rc('ytick', labelsize=18) 

fig, ax = plt.subplots(layout="constrained",sharex=True)



x = np.linspace(-1,1,1000)

P0 = sc.legendre(0)
P1 = sc.legendre(1)
P2 = sc.legendre(2)
P3 = sc.legendre(3)
P4 = sc.legendre(4)
P5 = sc.legendre(5)


ax.set_ylabel(r'$P_n(x)$',fontsize=20)
ax.set_xlabel(r'$x$',fontsize=22)
#ax.set_title('Polinomios de Legendre',fontsize=18)

ax.set_ylim(-1.5,1.2)

ax.plot(x,P0(x),color="black",lw=1.5) 
ax.plot(x,P1(x),color="red",lw=1.5)
ax.plot(x,P2(x),color="green",lw=1.5)
ax.plot(x,P3(x),color="blue",lw=1.5)
ax.plot(x,P4(x),color="orange",lw=1.5)
ax.plot(x,P5(x),color="pink",lw=1.5)


#ax.plot(x,P0(x),x,P1(x),x,P2(x),x,P3(x),x,P4(x),x,P5(x))

ax.legend((r'$P_0(x)$',r'$P_1(x)$',r'$P_2(x)$',r'$P_3(x)$',r'$P_4(x)$',r'$P_5(x)$'),
          shadow=True, loc="lower right", handlelength=1.5, fontsize=18)
          
ax.grid()

plt.savefig("../Figuras/5.1_Polinomios_Legendre.png",dpi=400)

plt.show()




