import numpy as np
import matplotlib.pyplot as plt

datos = np.loadtxt("Canal_ionico.txt")
salida = np.loadtxt("salida.txt")
radio = salida[:,2]
rmax = np.amax(radio)
I = np.argmax(radio)
cenx = salida[I, 0]
ceny = salida[I, 1]
plt.figure(figsize=(5,5))
circle = plt.Circle((cenx,ceny),rmax,color='b',fill=False)
ax = plt.gca()
ax.cla()
ax.set_xlim(-10,20)
ax.set_ylim(-10,20)
ax.plot((cenx),(ceny),'o', color ='r')
ax.add_artist(circle)
plt.scatter(datos[:,0], datos[:,1])
plt.xlabel("X (Amstrong)")
plt.ylabel("Y (Amstrong)")
plt.title("Param.: "+"x $=$ "+str(round(cenx,3))+", y $=$ "+str(round(ceny,3))+", radio $=$ "+str(round(rmax,3)), fontsize = 12)
plt.grid(True)
plt.savefig("Cmax.png")
plt.close()


datos1 = np.loadtxt("Canal_ionico1.txt")
salida1 = np.loadtxt("salida1.txt")
radio1 = salida1[:,2]
rmax1 = np.amax(radio1)
I1 = np.argmax(radio1)
cenx1 = salida1[I1, 0]
ceny1 = salida1[I1, 1]
plt.figure(figsize=(5,5))
circle1 = plt.Circle((cenx1,ceny1),rmax1,color='b',fill=False)
ax = plt.gca()
ax.cla()
ax.set_xlim(-10,20)
ax.set_ylim(-10,20)
ax.plot((cenx1),(ceny1),'o', color ='r')
ax.add_artist(circle1)
plt.scatter(datos1[:,0], datos1[:,1])
plt.xlabel("X (Amstrong)")
plt.ylabel("Y (Amstrong)")
plt.title("Param.: "+"x $=$ "+str(round(cenx1,3))+", y $=$ "+str(round(ceny1,3))+", radio $=$ "+str(round(rmax1,3)), fontsize = 12)
plt.grid(True)
plt.savefig("Cmax1.png")
plt.close()



plt.figure(figsize=(5,5))
plt.hist(salida[:,0], 50)
plt.xlabel("X (Amstrong)")
plt.ylabel("Frec. (AD)")
plt.title("Hist. para X en Canal I.")
plt.grid(True)
plt.savefig("xh.png")
plt.close()

plt.figure(figsize=(5,5))
plt.hist(salida[:,1], 50)
plt.xlabel("Y (Amstrong)")
plt.ylabel("Frec. (AD)")
plt.title("Hist. para Y en Canal I.")
plt.grid(True)
plt.savefig("yh.png")
plt.close()


plt.figure(figsize=(5,5))
plt.hist(salida1[:,0], 50)
plt.xlabel("X (Amstrong)")
plt.ylabel("Frec. (AD)")
plt.title("Hist. para X en Canal I. $1$")
plt.grid(True)
plt.savefig("xh1.png")
plt.close()

plt.figure(figsize=(5,5))
plt.hist(salida1[:,1], 50)
plt.xlabel("Y (Amstrong)")
plt.ylabel("Frec. (AD)")
plt.title("Hist. para Y en Canal I. $1$")
plt.grid(True)
plt.savefig("yh1.png")
plt.close()








