import numpy               as np
import matplotlib.pyplot   as plt
import scipy.special       as sc
import matplotlib          as mpl

mpl.rc('figure',  figsize=(14, 8))
mpl.rc('xtick', labelsize=21) 
mpl.rc('ytick', labelsize=21) 

x = np.linspace(0,50,1000)
J0 = sc.jv(0,x)
J1 = sc.jv(1,x)
J2 = sc.jv(2,x)
xi =0.2
J0xi = sc.jv(0,xi*x)
J1xi = sc.jv(1,xi*x)
J2xi = sc.jv(2,xi*x)

N0 = sc.yv(0,x)
N1 = sc.yv(1,x)
N2 = sc.yv(2,x)

N0xi = sc.yv(0,xi*x)
N1xi = sc.yv(1,xi*x)
N2xi = sc.yv(2,xi*x)



F0 = J0*N0xi-N0*J0xi
F1 = J1*N1xi-N1*J1xi
F2 = J2*N2xi-N2*J2xi

cerosF0 = []
ind0=[]
for i in range(1,len(F0)):
   if(F0[i]*F0[i-1]<0):
      ind0.append(i)
      cerosF0.append(x[i])
   

cerosF1 = []
ind1=[]
for i in range(1,len(F1)):
   if(F1[i]*F1[i-1]<0):
      ind1.append(i)
      cerosF1.append(x[i])
   

cerosF2 = []
ind2=[]
for i in range(1,len(F2)):
   if(F2[i]*F2[i-1]<0):
      ind2.append(i)
      cerosF2.append(x[i])
   

print(cerosF0)
print(F0[ind0])



fig, ax = plt.subplots(layout="constrained")

ax.set_ylabel(r'$F_m(x;\xi)$',fontsize=22)
ax.set_xlabel(r'$x$',fontsize=24)
#ax.set_title(r'Funciones $F_m(x;\xi)$',fontsize=20)

ax.plot(x,J0*N0xi-N0*J0xi,color="black",lw=1.5)
ax.plot(x,J1*N1xi-N1*J1xi,color="red",lw=1.5)
ax.plot(x,J2*N2xi-N2*J2xi,color="green",lw=1.5)
ax.plot(x,np.zeros(len(x)),color="grey",lw=1.5)

#ax.plot(x,J0*N0xi-N0*J0xi,x,J1*N1xi-N1*J1xi,x,J2*N2xi-N2*J2xi)

ax.legend((r'$F_0(x;0.2)$',r'$F_1(x;0.2)$',r'$F_2(x;0.2)$'),
          shadow=True, loc="lower left", handlelength=1.5, fontsize=22)
          
ax.grid()




x1, y1 = 0, -0.2
x2, y2 = 50,  0.2
#x1, x2, y1, y2 = -7, 4.3, 0, -4.3  # subregion of the original image
#axins = ax.inset_axes(
#    [0.3, 0.1, 0.7, 0.4],
#    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[-16,-14,-12,-10,-8,-6,-4,-2,0], yticklabels=[])


axins = ax.inset_axes(
    [0.3, 0.1, 0.67, 0.5],
    xlim=(x1, x2), ylim=(y1, y2))
axins.plot(x,J0*N0xi-N0*J0xi,color="black",lw=1.5)
axins.plot(x,J1*N1xi-N1*J1xi,color="red",lw=1.5)
axins.plot(x,J2*N2xi-N2*J2xi,color="green",lw=1.5)
axins.plot(x,np.zeros(len(x)),color="grey",lw=1.5)


axins.grid()
ax.indicate_inset_zoom(axins, edgecolor="orange")



## Guardamos la figura
plt.savefig("../Figuras/4.10_Raices_Fm-Bessel.png",dpi=400)




plt.show()