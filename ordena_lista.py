lista = [999,547,985,412,685,78,9,25]

#print(sorted(lista))

for i in range(len(lista)):
    
    menor = i

    for j in range(i+1,len(lista)):
        if lista[j] < lista[menor]:
            menor = j

    if lista[i] != lista[menor]:
        aux = lista[i]
        lista[i] = lista[menor]
        lista[menor] = aux

print(lista)