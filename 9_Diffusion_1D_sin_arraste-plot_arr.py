import numpy as np
import matplotlib.pyplot as plt
import matplotlib          as mpl

mpl.rc('figure',  figsize=(12, 5))
mpl.rc('xtick', labelsize=18) 
mpl.rc('ytick', labelsize=18) 

L  = 1
M  = 1
x0 = 0.5
D = 0.1
J = 3.0

def rho(x,t):
   suma = 1
   for n in range(1,200):
      kn = 2*n*np.pi/L
      suma+= np.cos(kn*(x-x0)- J*kn*t)*np.exp(-D*kn*kn*t)   
   return(suma)
   
    
   
   
x = np.linspace(0,L,1000)

fig, ax = plt.subplots(layout="constrained")


ax.set_ylabel(r'$\rho(x,t)$',fontsize=20)
ax.set_xlabel(r'$x$',fontsize=16)
#ax.set_title('$t=10^{-3}$',fontsize=20)
#ax.plot(x,rho(x,0.0001), x,rho(x,0.001),x,rho(x,0.01),x,rho(x,0.1))
ax.plot(x,rho(x,0.0001),color="black",lw=1.5) 
ax.plot(x,rho(x,0.001),color="red",lw=1.5)
ax.plot(x,rho(x,0.01),color="green",lw=1.5)
ax.plot(x,rho(x,0.1),color="blue",lw=1.5)


ax.set_ylim(0,20)
ax.legend((r'$t=10^{-4}$',r'$t=10^{-3}$',r'$t=10^{-2}$',r'$t=10^{-1}$'), shadow=True, loc=(0.8, 0.15), handlelength=1.5, fontsize=16)
          
ax.grid()

#############################################
## guardamos la figura
plt.savefig("../Figuras/GraphSolDiff1D_con_arrastre.png",dpi=400)

plt.show()




