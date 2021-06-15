print("A program a beírt számokat adja össze addig, míg 10-nél kisebbeket írunk be.")
szumma = 0
szám = 1
számláló = 0
while szám < 10:
    számláló += 1
    if számláló == 1 or számláló ==5 or (számláló>49 and számláló <60):
        névelő = "az"
    else:
        névelő = "a"
    szöveg = "Írd be " + névelő + " " + str(számláló) + ". számot! "
    szám = int(input(szöveg))
    szumma += szám
print("Az összeg:", szumma-szám)
