import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sc
import matplotlib          as mpl

mpl.rc('figure',  figsize=(14, 5))
mpl.rc('xtick', labelsize=21) 
mpl.rc('ytick', labelsize=21) 

x = np.linspace(0,50,1000)
n = 0
Jn = sc.jv(n,x)
alpha = sc.jn_zeros(n, 15)

print(alpha)

cero = 0*x

fig, ax = plt.subplots(layout="constrained")

ax.set_ylabel(r'$J_0(x)$',fontsize=20)
ax.set_xlabel(r'$x$',fontsize=20)
#ax.set_title('Raíces de la función de Bessel de orden cero',fontsize=20)


ax.set_xticks([alpha[0], alpha[1], alpha[2], alpha[3], alpha[4], alpha[5], alpha[6], alpha[7], alpha[8], alpha[9], alpha[10], alpha[11], alpha[12], alpha[13], alpha[14]])
ax.set_xticklabels([r'$\alpha_{_{0,1}}$', r'$\alpha_{_{0,2}}$',r'$\alpha_{_{0,3}}$',r'$\alpha_{_{0,4}}$',r'$\alpha_{_{0,5}}$',r'$\alpha_{_{0,6}}$',r'$\alpha_{_{0,7}}$',r'$\alpha_{_{0,8}}$',r'$\alpha_{_{0,9}}$',r'$\alpha_{_{0,10}}$',r'$\alpha_{_{0,11}}$',r'$\alpha_{_{0,12}}$',r'$\alpha_{_{0,13}}$',r'$\alpha_{_{0,14}}$',r'$\alpha_{_{0,15}}$'], color="black", size=22)

ax.plot(x,Jn,'b')
ax.plot(x,cero,'black',markersize =1)

ax.set_xlim(-0.1,50.1)

#ax.legend((r'$J_0(x)$'), shadow=True, loc=(0.8, 0.48), handlelength=1.5, fontsize=16)
          
ax.grid()

plt.savefig("../Figuras/4.3_Racices_BesselJ0.png",dpi=400)

plt.show()