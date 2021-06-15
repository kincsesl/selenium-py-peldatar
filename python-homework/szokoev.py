def szökőév(ev):
    if ev % 4 != 0:
        return False
    elif ev % 100 == 0 and ev % 400 !=0:
        return False
    else:
        return True

print("2100. szökőév? ", szökőév(2100))

try:
    évszám = int(input("Írj be egy évszámot 0-9999 között: "))
except ValueError:
    print("Ez nem szám, próbáld újra!")
except:
    print("Egyéb hiba, próbáld újra!")
    

if szökőév(évszám):
    print(évszám, ". szökőév.")
else:
    print(évszám, ". nem szökőév.")    
