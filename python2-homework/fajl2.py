lista = []

with open("text.txt", "r") as fájl:
    for sor in fájl:
        sor = sor.replace("\n", "")
        lista.append(sor)
    
for i in lista:
    print(i, end = " ")
