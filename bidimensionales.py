import numpy as np

arreglo = np.array([[4,5,8,7],[6,3,4,5]])

print(arreglo)
#print(arreglo[1,2])

for x in range(len(arreglo)):
    for y in range(len(arreglo[x])):
        print(f"{arreglo[x,y]}")