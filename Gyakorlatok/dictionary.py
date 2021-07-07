l = [1, 5, 3, 7, 8, 6, 3]  # A listánál a sorrend fontos. Referenciák gyűjteménye.

# További konténertípusok (ezek is referenciák):

# tuple, konstans lista

t = (1, 5, 3, 7, 8, 6, 3)  # Fontos a sorrend, és nem lehet változtatni rajta.
print(t)

t = (7, 8, 6, 3)  # Fontos a sorrend, és nem lehet változtatni rajta.
print(t)

tmp_list = list(t)
# A tmp_list-et változtathatom.
t = tuple(tmp_list)

# Dictionary
d = {"név": "Tamás", "kor": "kerederek", "irsz": 2143}

d = {"név": "Tamás",
     "kor": "kerederek",
     "address": {"irsz": 2143}
     }

# Set: minden elem max. egyszer [egyedi]... kapcsos {}

s = {2, 5, 2, 2, 4}
print(s)

lista1 = list(set(l))