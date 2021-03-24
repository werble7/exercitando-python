px = float(input("insira a coordenada x do ponto p: "))
py = float(input("insira a coordenada y do ponto p: "))
qx = float(input("insira a coordenada x do ponto q: "))
qy = float(input("insira a coordenada y do ponto q: "))
import cmath
distancia = (qx - px) ** 2 + (qy - py) ** 2
raiz = distancia ** 0.5
print("a distância é ", raiz)
