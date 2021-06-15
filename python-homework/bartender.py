print("Önkiszolgáló boltunkban egyelőre csak sör és kóla kapható.")
kor = int(input("Éveinek száma: "))
pia = input("Mit iszik [sör/kóla]: ")
if pia == "sör":
    if kor >=18:
        print("Itt a söre.")
    else:
        print("Kicsi vagy még ehhez!")
elif pia == "kóla":
    if kor > 60:
        print("A koffein megemelheti a vrényomást, de itt a kólája.")
    else:
        print("Itt a kólája")
else:
    print("Mondtam, hogy csak sör és kóla van!")
