with open("text.txt", "r") as fájl:
    with open("text5.txt", "w") as fájl2:
        for sor in fájl:            
            fájl2.write(sor)

        
