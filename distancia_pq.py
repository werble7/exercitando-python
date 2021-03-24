px = float(input("insira a coordenada x do ponto p: "))
py = float(input("insira a coordenada y do ponto p: "))
qx = float(input("insira a coordenada x do ponto q: "))
qy = float(input("insira a coordenada y do ponto q: "))
distancia = ((qx - px) ** 2 + (qy - py) ** 2) ** 0.5
print("a distância entre p e q é ", distancia)
