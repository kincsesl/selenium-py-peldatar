lista = []

with open("text.txt", "r") as fájl:
    for sor in fájl:
        sor = sor.replace("\n", "")
        lista.append(sor)

with open("text2.txt", "w") as fájl:
    for sor in lista:
        sor +=" "
        fájl.write(sor)
        
