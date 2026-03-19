# Plane Classes
# Defines a Plane class and creates two plane objects.

class Plane:
    def __init__(self, name, sp, wt, acc, hnd):
        self.name = name
        self.sp = sp
        self.wt = wt
        self.acc = acc
        self.hnd = hnd

plane_1 = Plane("Boeing 747", 500, 4400, 10, 100)
plane_2 = Plane("harrier", 200, 500, 5, 10)

planes = [plane_1, plane_2]

for x in planes:
    print(x.name)
