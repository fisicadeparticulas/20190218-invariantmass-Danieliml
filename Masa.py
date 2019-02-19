import matplotlib.pyplot as plt
import math

F = open("Datos.csv","r")

q = []
M = []
L =F.readlines()
L[0] = L[0].split(",")
#print(len(L[0]))

for i in range(1,100001):
	L[i] = L[i].split(",")

	aux = 4
	P1 = 0.0
	for j in range(0,3):
		P1 += float(L[i][aux])**2
		aux += 1
	P1 = math.sqrt(P1)

	aux = 13
	P2 = 0.0
	for j in range(0,3):
		P2 += float(L[i][aux])**2
		aux *= 1
	P2 = math.sqrt(P2)

	E1 = float(L[i][3])
	E2 = float(L[i][12])

	if (E1 + E2)**2 - (P1 + P2)**2 > 0:
		M += [math.sqrt((E1 + E2)**2 - (P1 + P2)**2)]

	#M += [math.sqrt((E1 + E2)**2 - (P1 + P2)**2)]


#mos = [int(random()*100) for _ in range(3000)]

print(max(M))
print(min(M))


print(q)
plt.title('Masa')
plt.hist(M)
plt.grid(True)
plt.show()
plt.clf()
#print(M)







