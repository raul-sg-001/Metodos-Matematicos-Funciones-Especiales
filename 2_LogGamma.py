import numpy               as np
import matplotlib.pyplot   as plt
import scipy.special       as sc
import matplotlib          as mpl

mpl.rc('figure',  figsize=(12, 5))
mpl.rc('xtick', labelsize=18) 
mpl.rc('ytick', labelsize=18) 

################################################
### definimos las funciones a graficar
x        = np.linspace(-5.5,8,100000)
xm       = np.linspace(1.0001,8,100000)

f0       = np.log(np.absolute(sc.gamma(x)))
f1       = 0.5*np.log(2*np.pi*(xm-1)) + (xm-1)*np.log((xm-1)*np.exp(-1.0))

#f2       = sc.polygamma(2, x)



################################################
################################################
###         GRAFICAMOS LAS FUNCIONES
###           ** UN SOLO PANEL **

fig, ax = plt.subplots(layout="constrained")

#############################################
## aquí agregamos aspectos adicionales del plot
ax.grid()     ## malla en color gris
#ax.plot(x,0*x,color='gray',lw=1.0)  ## línea de referencia origen


#############################################
## aquí agregamos los encabezados y las etiquetas de los ejes
ax.set_title('Logaritmo de la función gamma',fontsize=20)
ax.set_ylabel(r'$\text{ln}(|\Gamma(x)|)$',fontsize=20)
ax.set_xlabel(r'$x$',fontsize=20)


#############################################
## aquí modificamos límites en los ejes 
ax.set_ylim(-5,12)
ax.set_xlim(-5.1,7.1)


#############################################
## aquí agregamos las demás funciones
ax.plot(x,f0,color = 'black',lw=1.5)
ax.plot(xm,f1,color = 'red',lw=1.50)
#ax.plot(x,f2,color = 'blue',lw=1.0)
#############################################

#############################################
## aquí agregamos "legends"
ax.legend((r'$\text{ln}(|\Gamma(x)|)$','Fórmula de Stirling'),
          shadow=True, loc="upper right", handlelength=1.5, fontsize=18)

#ax.legend((r'$\Psi^{(0)}(x)$',r'$\Psi^{(1)}(x)$',r'$\Psi^{(2)}(x)$'),
#          shadow=True, loc=(0.7, 0.08), handlelength=1.5, fontsize=12)


#############################################
## guardamos la figura
plt.savefig("../Figuras/GraficaLogGamma.png",dpi=400)
plt.show()




