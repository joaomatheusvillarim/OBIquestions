import math
ndepredios = int(input())
alturas = input().split()
lista = []
y = 0
for x in alturas:
        x = int(x)
        lista.append([x, y])
        y += 1

distancia = 0
for x in lista:
    for y in lista:
        distanciaEntrePredios = abs(x[1] - y[1])
        calculo = int(x[0]) + int(y[0]) + int(distanciaEntrePredios)
        if calculo > distancia:
            distancia = calculo
        else:
            pass

print(distancia)