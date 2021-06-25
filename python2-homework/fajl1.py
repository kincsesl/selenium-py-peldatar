lista = []

with open("text.txt", "r") as fájl:
    for sor in fájl:
        sor = sor.replace("\n", "")
        print(sor, end=" ")
    
