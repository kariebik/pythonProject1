class Vector:

    def __init__(self, x, y):
        self.x = []
        self.y = []

        for i in range(x+1):
            self.x.append(i)
        for i in range(y+1):
            self.y.append(i)



    def __repr__(self):
        return '(' + str(self.x[-1]) + ',' + str(self.y[-1]) + ')'

    def __add__(self, other):
        new_x = self.x[-1] + other.x[-1]
        yy = self.y[-1] + other.y[-1]
        return Vector(new_x, yy)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __sub__(self, other):
        new_x = self.x[-1] - other.x[-1]
        yy = self.y[-1] - other.y[-1]
        return Vector(new_x, yy)

    def __getitem__(self, index):
        if index == 0:
            return self.x[-1]
        elif index == 1:
            return self.y[-1]
        return IndexError

    def __mul__(self, other):
        if isinstance(other, int):
            new_x = self.x[-1] * other
            yy = self.y[-1] * other
            return Vector(new_x, yy)
        elif isinstance(other, Vector):
            new_x = self.x[-1] * other.x[-1]
            yy = self.y[-1] * other.y[-1]
            return new_x +yy
        else:
            return ValueError

    def __setitem__(self, key, value):
        if key == 0:
           self.x = value
        elif key == 1:
            self.y = value

try:
    print(Vector(8, 6))
except ValueError:
    print("must be an integer or vector")
except IndexError:
    print("must but a 1 or 0")