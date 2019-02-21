import matplotlib.pyplot as plt
import math

F = open("Datos.csv","r")

M = []
L =F.readlines()
L[0] = L[0].split(",")

for i in range(1,100001):
	L[i] = L[i].split(",")

	aux = 4
	P = 0.0
	for j in range(0,3):
		P += (float(L[i][aux])+float(L[i][aux+9]))**2
		aux += 1
	P = math.sqrt(P)
	
	E1 = float(L[i][3])
	E2 = float(L[i][12])

	if (E1+E2)**2 - P**2 > 0:
		M += [math.sqrt((E1+E2)**2 - P**2)]
	
print(max(M))
print(min(M))

plt.title('Masa')
plt.hist(M)
plt.grid(True)
plt.show()
plt.clf()








