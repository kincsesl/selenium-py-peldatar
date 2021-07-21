class Point:
    def __init__(self, xx=0, xy=0):
        self.x = xx
        self.y = xy

    def távolság(self):
        return ((self.x ** 2 + self.y ** 2) ** .5)

    def feleút(self, pont2):
        mx = self.x / 2 + pont2.x / 2
        my = self.y / 2 + pont2.y / 2
        return Point(mx, my)

    def __str__(self):
        return f'x = {self.x}, y = {self.y}'


p = Point(5, 12)
q = Point(22, 44)
print(p.feleút(q))
