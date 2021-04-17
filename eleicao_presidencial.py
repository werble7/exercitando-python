cand1 = 0
cand2 = 0
cand3 = 0
nulo = 0
branco = 0
while True:
    print("digite [1],[2] ou [3] para seu candidato, [5] nulo e [6] branco: ")
    voto = int(input())
    if voto == 1:
        cand1 = cand1 + 1
    elif voto == 2:
        cand2 = cand2 + 1
    elif voto == 3:
        cand3 = cand3 + 1
    elif voto == 5:
        nulo = nulo + 1
    elif voto == 6:
        branco = branco + 1
    else:
        break

if nulo > cand1 and nulo > cand2 and nulo > cand3:
    print("eleição inválida, terá refação")
elif cand1 > cand2 and cand1 > cand3:
    cand1 = cand1 + branco
    print("candidato 1 eleito")
elif cand2 > cand1 and cand2 > cand3:
    cand2 = cand2 + branco
    print("candidato 2 eleito")
elif cand3 > cand1 and cand3 > cand1:
    cand3 = cand3 + branco
    print("candidato 3 eleito")
else:
    print("eleição inválida, terá refação")

total = cand1 + cand2 + cand3 + nulo + branco
pct_nulo = nulo / total * 100
pct_branco = branco / total * 100

print("candidato 1, votos: {0} \ncandidato 2, votos: {1} \ncandidato 3, votos: {2} \nnulo, votos: {3} \nbranco, votos: {4}".format(cand1, cand2, cand3, nulo, branco))
print("porcentagem de nulos: {0} \nprocentagem de brancos: {1}".format(pct_nulo, pct_branco))
