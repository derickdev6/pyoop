class Coordinates():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((self.x - other.x)**2+(self.y - other.y)**2)**.5


if __name__ == '__main__':
    c1 = Coordinates(3, 30)
    c2 = Coordinates(4, 8)

    print(f'Distance from c1 to c2 is {round(c1.distance(c2),3)}')
    assert(isinstance(c1, Coordinates))
    assert not (isinstance(10, Coordinates))
