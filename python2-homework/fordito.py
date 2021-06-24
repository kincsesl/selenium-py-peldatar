szám = 1
lista = []

while szám >0:
    szám = int(input("Írj be egy pozitív számot, 0-ra vége a játéknak: "))
    lista.append(szám)

lista.remove(0)
lista.reverse()
print(lista)
