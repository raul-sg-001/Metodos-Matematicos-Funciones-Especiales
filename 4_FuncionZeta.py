
import  numpy               as      np
import  matplotlib.pyplot   as      plt
from    scipy.special       import  zeta
import  matplotlib          as      mpl
#import  mpmath

mpl.rc('figure',  figsize=(12, 7))
mpl.rc('xtick', labelsize=18) 
mpl.rc('ytick', labelsize=18) 

################################################
### definimos las funciones a graficar
x        = np.linspace(-20,5,10000)
f0       = zeta(x)

xext     = np.linspace(-22,7,10000)
xext2    = np.linspace(-100,100,10000)

#abs_vals = [abs(z) for z in zeta_vals]

y        = np.linspace(-50j,50j,10000)
yre      = np.linspace(-50,50,10000)
f1       = zeta(0.5+y)

"""
mpmath.dps = 15  # Precisión decimal
yre      = np.linspace(-50,50,10000)
y = np.linspace(-50, 50, 10000)
s = [mpmath.mpc(0.5, yi) for yi in y]
f1 = [mpmath.zeta(si) for si in s]
"""

################################################
################################################
###         GRAFICAMOS LAS FUNCIONES
###           ** DOS SOLO PANELES **

fig, ax = plt.subplots(2,layout="constrained",)
#props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)


#############################################
## aquí agregamos los encabezados y las etiquetas de los ejes
##     PANEL 1
ax[0].set_title('Función zeta de Riemann',fontsize=20)
ax[0].set_ylabel(r'$\zeta(x)$',fontsize=20)## se comenta por sharex=True

#############################################
## aquí agregamos los encabezados y las etiquetas de los ejes
##     PANEL 2
ax[1].set_ylabel(r'$\zeta(0.5+ix)$',fontsize=20)
ax[1].set_xlabel(r'$x$',fontsize=20)  


ax[0].text(0.015,0.20,"(a)",transform=ax[0].transAxes,fontsize=35,color="black",verticalalignment='top')
ax[1].text(0.015,0.20,"(b)",transform=ax[1].transAxes,fontsize=35,color="black",verticalalignment='top')


#############################################
## aquí modificamos límites en los ejes 

###    PANEL 1
ax[0].set_ylim(-3,6)
ax[0].set_xlim(-21,6)

#ax[0].set_ylim(-400,400)
#ax[0].set_xlim(0,100)

###    PANEL 2
ax[1].set_ylim(-5,4)
ax[1].set_xlim(-55,55)


#############################################
## aquí agregamos las funciones
ax[0].plot(x,np.real(f0),color = 'black',lw=1.50)
ax[0].plot(xext,np.zeros(len(xext)),color = 'gray',lw=1.50)


x1, y1 = -15, -0.1
x2, y2 = -1,  0.1
#x1, x2, y1, y2 = -7, 4.3, 0, -4.3  # subregion of the original image
axins = ax[0].inset_axes(
    [0.2, 0.6, 0.5, 0.4],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[-16,-14,-12,-10,-8,-6,-4,-2,0], yticklabels=[])

axins.plot(x,np.real(f0),color = 'black',lw=1.50)
axins.plot(x,np.zeros(len(x)),color = 'gray',lw=1.50)
axins.grid()
ax[0].indicate_inset_zoom(axins, edgecolor="orange")



ax[1].plot(yre,np.real(f1),color = 'black',lw=1.50)
ax[1].plot(yre,np.imag(f1),color = 'red',lw=1.50)
#ax[1].plot(yre,np.zeros(len(y)),color = 'gray',lw=1.50)
ax[1].plot(xext2,np.zeros(len(xext2)),color = 'gray',lw=1.50)

#############################################

#############################################
## aquí agregamos "legends"
#ax[0].legend(r'Re[ $\zeta(0.5+ ix)$ ]',shadow=True, loc="lower right", handlelength=1.5, fontsize=16)
ax[1].legend((r'Re[ $\zeta(0.5+ix)$ ]',r'Im[ $\zeta(0.5+ix)$ ]'),
          shadow=True, loc="lower right", handlelength=1.5, fontsize=16)



#ax.legend((r'$\Psi^{(0)}(x)$',r'$\Psi^{(1)}(x)$',r'$\Psi^{(2)}(x)$'),
#          shadow=True, loc=(0.7, 0.08), handlelength=1.5, fontsize=12)

#############################################
## aquí agregamos aspectos adicionales del plot
ax[0].grid()     ## malla en color gris
ax[1].grid()     ## malla en color gris
##ax.plot(x,0*x,'--r')  ## línea de referencia origen


#############################################
## guardamos la figura
plt.savefig("Funcion_zeta.png",dpi=400)
plt.show()






