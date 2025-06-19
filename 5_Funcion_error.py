import  numpy               as      np
import  matplotlib.pyplot   as      plt
from    scipy.special       import  erf,erfc, erfinv, erfi, dawsn
import  matplotlib          as      mpl

mpl.rc('figure',  figsize=(12, 5))
mpl.rc('xtick', labelsize=18) 
mpl.rc('ytick', labelsize=18) 

################################################
### definimos las funciones a graficar
x        = np.linspace(-5,5,10000)

f0       = erf(x)
f1       = erfc(x)
f4       = dawsn(x)

f2       = erfinv(x)
f3       = erfi(x)



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
ax.set_title('Función error y funciones relacionadas ',fontsize=20)
ax.set_ylabel(r'$\text{erf}(x)$, $\text{erfc}(x)$, $D^+(x)$',fontsize=18)
ax.set_xlabel(r'$x$',fontsize=20)


#############################################
## aquí modificamos límites en los ejes 
#ax.set_ylim(-5,12)
#ax.set_xlim(-5.1,7.1)


#############################################
## aquí agregamos las demás funciones
ax.plot(x,f0,color = 'black',lw=1.5)
ax.plot(x,f1,color = 'blue',lw=1.5)
#ax.plot(x,f2,color = 'green',lw=1.0)
#ax.plot(x,f3,color = 'red',lw=1.0)
ax.plot(x,f4,color = 'green',lw=1.5)
#############################################

#############################################
## aquí agregamos "legends"
ax.legend((r'erf$(x)$','erfc$(x)$',r'D^+(x)'),
          shadow=True, loc="upper right", handlelength=1.5, fontsize=18)

#ax.legend((r'$\Psi^{(0)}(x)$',r'$\Psi^{(1)}(x)$',r'$\Psi^{(2)}(x)$'),
#          shadow=True, loc=(0.7, 0.08), handlelength=1.5, fontsize=12)


#############################################
## guardamos la figura
plt.savefig("../Figuras/GraficaFuncionError.png",dpi=400)
plt.show()




