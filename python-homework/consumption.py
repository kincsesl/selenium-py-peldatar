#Konstans adatookkal
városi_f = 9
országúti_f = 7
városi_km = 35
országúti_km = 170
eredmény = str(városi_km*városi_f/100 + országúti_km*országúti_f/100)
eredmény = eredmény.replace(".", ",")
print("A fogyasztás 170 km országúton és 35 km városi úton:", eredmény, "l")
#Input adatokkal
városi_f = int(input("Mennyit eszik a verda városban (l)? "))
országúti_f = int(input("Mennyit eszik a verda országúton (l)? "))
városi_km = int(input("Hány km-t mész városban? "))
országúti_km = int(input("Hány km-t mész országúton? "))
eredmény = városi_km*városi_f/100 + országúti_km*országúti_f/100
eredmény = str(eredmény)
eredmény = eredmény.replace(".", ",")
print("A fogyasztás", országúti_km, "km országúton és", városi_km, "km városi úton:", eredmény, "l")
