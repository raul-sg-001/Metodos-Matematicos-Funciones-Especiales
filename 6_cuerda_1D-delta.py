import numpy               as np
import matplotlib.pyplot   as plt 
import matplotlib          as mpl

mpl.rc('figure',  figsize=(12, 7))
mpl.rc('xtick', labelsize=18) 
mpl.rc('ytick', labelsize=18) 

c  = 1.0
L  = 1.0
x0 = 0.5 
def psi(x,t):
   suma = 0
   for n in range(1,10000):
      kn      = n*np.pi/L
      omegan  = kn*c
      suma   += 2.0*np.sin(kn*x0)*np.sin(kn*x)*np.cos(omegan*t)/L
   return(suma)

x = np.linspace(0,L,5000)


fig, ax = plt.subplots(2, layout = "constrained",sharex=True)

ax[0].set_ylabel(r'$\psi(x,t)$',fontsize=20)
ax[1].set_ylabel(r'$\psi(x,t)$',fontsize=20)

ax[0].set_xlabel(r'$x$',fontsize=20)
#ax[1].set_xlabel(r'$x$',fontsize=20)

#ax.set_title('$t=10^{-3}$',fontsize=20)
ax[0].plot(x,psi(x,0.0001),color="black",lw =1.5)
ax[0].plot(x,psi(x,0.2006),color="red",lw =1.5)
ax[0].plot(x,psi(x,0.7008),color="blue",lw =1.5)


ax[1].plot(x,psi(x,0.00001),color="black",lw =1.5)
ax[1].plot(x,psi(x,0.01006),color="red",lw =1.5)
ax[1].plot(x,psi(x,0.1008),color="blue",lw =1.5)


ax[0].text(0.015,0.20,"(a)",transform=ax[0].transAxes,fontsize=35,color="black",verticalalignment='top')
ax[1].text(0.015,0.20,"(b)",transform=ax[1].transAxes,fontsize=35,color="black",verticalalignment='top')


ax[1].set_ylim(-10,10)
ax[1].set_xlim(-0.050,1.05)
ax[1].legend( (r'$t=10^{-4}$',r'$t=0.20$',r'$t=0.70$'), shadow=True, loc="lower right", handlelength=1.5, fontsize=18)

ax[0].set_ylim(-150,150)
ax[0].set_xlim(-0.050,1.05)
ax[0].legend( (r'$t=10^{-4}$',r'$t=0.20$',r'$t=0.70$'), shadow=True, loc="lower right", handlelength=1.5, fontsize=18)

 
ax[0].grid()
ax[1].grid()
plt.savefig("../Figuras/3.2_EvolucionOnda1D-delta.png",dpi=400)

plt.show()