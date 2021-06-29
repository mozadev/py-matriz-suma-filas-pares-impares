# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 08:46:44 2021

@author: Guillermo Hondermann
"""


import random

m=int(input('Numero de filas: '))
while not m>1:
    m = int(input('Numero de filas: '))

n=int(input('Numero de columnas: '))
while not m>1:
    n = int(input('Numero de columnas: '))


M=[]
suma=0
for i in range(m):
    M.append([0]*n)

for i in range(m):
    for j in range(n):
        elementoMatriz=random.randint(10,99)
        if elementoMatriz % 3==0:
            M[i][j]=elementoMatriz
        suma=suma+M[i][j]

for i in range(m):
    for j in range(n):
        print(M[i][j],end='\t')
    print()


suma_filas_pares=0
suma_filas_inpares=0
for i in range(m):
    for j in range(n):
        if i%2==0:
            suma_filas_pares=suma_filas_pares+ M[i][j]
        if i % 2 != 0:
            suma_filas_inpares = suma_filas_inpares + M[i][j]
            
            
    print()

print('Suma:',suma)
print('Suma filas pares:',suma_filas_pares)
print('Suma filas impares:',suma_filas_inpares)
