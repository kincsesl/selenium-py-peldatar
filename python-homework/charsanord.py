a, z = 97, 122
n = int(input("Hány sor legyen (1-10)? "))
#for n in range(1, 11):            
tömb = [0 for j in range(n+1)]
for i in range(n):
    tömb[i] = ""
print(n)
for i in range(a, z+1):
    tömb[i%n] += chr(i) + ":" + str(i)+" "
for j in range(a%n, a%n+n):
    print(tömb[j%n])
