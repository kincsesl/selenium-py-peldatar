# 1) Adott számokat tartalmazó lista.
# Pl. [11, 45, 8, 11, 23, 45, 23, 45, 89]
#
# Írj egy olyan Python programot ami egy asszociatív tömbben eltárolja a lista elemeinek előfordulási számát.
#
# A fenti példára a kimenet: {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

lista = [11, 45, 8, 11, 23, 45, 23, 45, 89]
szótár = {}
for elem in lista:
    szótár[elem] = szótár.get(elem, 0) + 1

print(szótár)

countDict = dict()
for item in lista:
    if(item in countDict):
        countDict[item] += 1
    else:
        countDict[item] = 1
print(countDict)

#Harmadik megoldás
l = [11, 45, 8, 11, 23, 45, 23, 45, 89]
d = {x: l.count(x) for x in l}
print(d)

lista = [{"kulcs": "érték"}, {"kulcs2": "érték2"}]
print(lista)

lista = [(1, 2, 3, 4), (2, 3, 4, 5, 6)]
print(lista)
lista.append((3, 2, 1, 6))
print(lista)