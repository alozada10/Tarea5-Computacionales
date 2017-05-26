import numpy as np
import matplotlib.pyplot as plt

Obs = np.loadtxt("CircuitoRC.txt")
t = Obs[:,0]
c = Obs[:,1]
v0= 10
Rw = np.empty((0))
Cw = np.empty((0))
Iw = np.empty((0))
Rw = np.append(Rw,5.0)
Cw = np.append(Cw,5.0)


def chi(mod,obs):
    chi = 0.5*sum(((obs-mod)/100)**2)
    a = np.exp(-chi)
    return a
    
def ec(R,C,t):
    a = v0*C*(1-np.exp(-t/(R*C)))
    return a

Q0 = ec(Rw[0],Cw[0],t)
Iw = np.append(Iw,chi(Q0,c))

for i in range(20000):
    Cp = np.random.normal(Cw[i], 0.1)
    Rp = np.random.normal(Rw[i], 0.1)
    Q0 = ec(Rw[i],Cw[i],t)
    cp = ec(Rp, Cp,t)
    Ip = chi(cp,c)
    I0 = chi(Q0,c)
    alpha = (Ip/I0)*1.0

    if(alpha>=1.0):
        Rw = np.append(Rw, Rp)
        Cw = np.append(Cw, Cp)
        Iw = np.append(Iw, Ip)     
    else:
        betha = np.random.uniform(0,1)
        if(betha<=alpha):
            Rw = np.append(Rw, Rp) 
            Cw = np.append(Cw, Cp)
            Iw = np.append(Iw, Ip)
        else:
            Rw = np.append(Rw, Rw[i])
            Cw = np.append(Cw, Cw[i])
            Iw = np.append(Iw, I0)
chiMax = np.argmax(Iw)
CC = Cw[chiMax]
CR = Rw[chiMax]
Cc = ec(CR, CC,t)


plt.figure(figsize=(5,5))
plt.scatter(Rw, -np.log(Iw),c="b",alpha = 0.4,s=8.9)
plt.xlabel("R (ohm)",fontsize=15)
plt.ylabel("Verosimilitud (AD)",fontsize=15)
plt.title("R verosimilitud",fontsize=20)
plt.grid(True)
plt.savefig("R_vero.jpg")
plt.close()

plt.figure(figsize=(5,5))
plt.scatter(Cw, -np.log(Iw),facecolor="b",alpha=0.4,s=8.9)
plt.xlabel("C (F)",fontsize=15)
plt.ylabel("Verosimilitud (AD)",fontsize=15)
plt.title("C  verosimilitud",fontsize=20)
plt.grid(True)
plt.savefig("C_vero.jpg")
plt.close()

plt.figure(figsize=(5,5))
plt.hist(Rw, 50, normed=1,alpha=0.7)
plt.xlabel("R (ohm)",fontsize =15)
plt.ylabel("Frec.",fontsize =15)
plt.title("Frec. normalizada para R",fontsize=20)
plt.grid(True)
plt.savefig("Rh.jpg")
plt.close()

plt.figure(figsize=(5,5))
plt.hist(Cw, 50, normed=1,alpha=0.7)
plt.xlabel("C (F)",fontsize=15)
plt.ylabel("Frec.",fontsize=15)
plt.title("Frec. normalizada para C",fontsize=20)
plt.grid(True)
plt.savefig("Ch.jpg")
plt.close()

plt.figure(figsize=(5,5))
plt.scatter(t, c, c="b",alpha=0.4,s=8.9,label="Observado")
plt.plot(t, Cc, c="r", label="Modelo con R $=$ "+str(round(CR,2)) +  "  y  C $=$ " +str(round(CC,2)))
plt.xlabel("Tiempo(s)",fontsize=15)
plt.ylabel("Carga(C)",fontsize=15)
plt.title("Q(t)",fontsize=20)
plt.grid(True)
plt.legend()
plt.savefig("DatModel.jpg")
plt.close()





