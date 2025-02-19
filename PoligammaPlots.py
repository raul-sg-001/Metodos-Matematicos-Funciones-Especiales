import numpy               as np
import matplotlib.pyplot   as plt
import scipy.special       as sc
import matplotlib          as mpl

mpl.rc('figure',  figsize=(12, 5))
mpl.rc('xtick', labelsize=18) 
mpl.rc('ytick', labelsize=18) 

################################################
### definimos las funciones a graficar
x        = np.linspace(-8.5,7.5,100000)
f0       = sc.polygamma(0, x)
f1       = sc.polygamma(1, x)
f2       = sc.polygamma(2, x)



################################################
################################################
###         GRAFICAMOS LAS FUNCIONES
###           ** UN SOLO PANEL **

fig, ax = plt.subplots(layout="constrained")


#############################################
## aquí agregamos los encabezados y las etiquetas de los ejes
ax.set_title('Función poligamma en variable real',fontsize=20)
ax.set_ylabel(r'$\Psi^{(m)}(x)$',fontsize=20)
ax.set_xlabel(r'$x$',fontsize=20)


#############################################
## aquí modificamos límites en los ejes 
ax.set_ylim(-80,100)
ax.set_xlim(-8.1,6.1)


#############################################
## aquí agregamos las demás funciones
ax.plot(x,f0,color = 'black',lw=1.0)
ax.plot(x,f1,color = 'red',lw=1.0)
ax.plot(x,f2,color = 'blue',lw=1.0)
#############################################

#############################################
## aquí agregamos "legends"
ax.legend((r'$\Psi^{(0)}(x)$',r'$\Psi^{(1)}(x)$',r'$\Psi^{(2)}(x)$'),
          shadow=True, loc="upper right", handlelength=1.5, fontsize=18)

#ax.legend((r'$\Psi^{(0)}(x)$',r'$\Psi^{(1)}(x)$',r'$\Psi^{(2)}(x)$'),
#          shadow=True, loc=(0.7, 0.08), handlelength=1.5, fontsize=12)

#############################################
## aquí agregamos aspectos adicionales del plot
ax.grid()     ## malla en color gris
##ax.plot(x,0*x,'--r')  ## línea de referencia origen


#############################################
## guardamos la figura
plt.savefig("../Figuras/GraficaPolygamma.png",dpi=400)
plt.show()

