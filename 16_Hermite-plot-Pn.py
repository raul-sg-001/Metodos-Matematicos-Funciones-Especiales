import numpy               as np
import matplotlib.pyplot   as plt
import scipy.special       as sc
import matplotlib          as mpl

mpl.rc('figure',  figsize=(12, 7))
mpl.rc('xtick', labelsize=18) 
mpl.rc('ytick', labelsize=18) 

fig, ax = plt.subplots(layout="constrained",sharex=True)


x = np.linspace(-10,10,1000)

P0 = sc.hermite(0)
P1 = sc.hermite(1)
P2 = sc.hermite(2)
P3 = sc.hermite(3)
P4 = sc.hermite(4)
P5 = sc.hermite(5)

ax.set_ylabel(r'$H_n(x)$',fontsize=20)
ax.set_xlabel(r'$x$',fontsize=22)
#ax.set_title('Polinomios de Legendre',fontsize=18)

ax.set_ylim(-45,45)
ax.set_xlim(-5,5)

ax.plot(x,P0(x),color="black",lw=1.5) 
ax.plot(x,P1(x),color="red",lw=1.5)
ax.plot(x,P2(x),color="green",lw=1.5)
ax.plot(x,P3(x),color="blue",lw=1.5)
ax.plot(x,P4(x),color="orange",lw=1.5)
ax.plot(x,P5(x),color="pink",lw=1.5)


ax.legend((r'$H_0(x)$',r'$H_1(x)$',r'$H_2(x)$',r'$H_3(x)$',r'$H_4(x)$',r'$H_5(x)$'),
          shadow=True, loc="lower right", handlelength=1.5, fontsize=18)

          
ax.grid()

plt.savefig("../Figuras/6.2_Polinomios_Hermite.png",dpi=400)

plt.show()






