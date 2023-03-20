import numpy as np
import csv

# Base -----------------------
a = np.loadtxt('Dados/a.csv', delimiter=';')
print("a:")
print(a)
m = np.loadtxt('Dados/M.csv', delimiter=';')
print("\nM:")
print(m)
n = np.loadtxt('Dados/N.csv', delimiter=';')
print("\nM:")
print(n)

# Auxiliar -------------------
aM = np.loadtxt('Dados/aM.csv', delimiter=';')
mN = np.loadtxt('Dados/MN.csv', delimiter=';')

        
# Multiplicação ---------------
resultadoaM = np.dot(a,m)
print(resultadoaM)

resultadoMN = np.dot(m,n)
print(resultadoMN)


# result = np.dot(a,M)