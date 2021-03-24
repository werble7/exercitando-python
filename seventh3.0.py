px = float(input("insira a coordenada x do ponto p: "))
py = float(input("insira a coordenada y do ponto p: "))
qx = float(input("insira a coordenada x do ponto q: "))
qy = float(input("insira a coordenada y do ponto q: "))
import cmath
distancia = (qx - px) ** 2 + (qy - py) ** 2
raiz = cmath.sqrt(distancia)
print("a distância é ", raiz)
# os três "seventh" deram iguais resultados, três jeitos de usar a raiz quadrada
