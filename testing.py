#python practice file

class Shape:

    shape_list = []

    def __init__(self, t):
        self.type = t
        self.shape_list.append(self)

    def __repr__(self):
        return self.type
    

def is_same(obj1, obj2):
    if obj1 is obj2:
        return True
    else:
        return False


square = Shape('square')
other_square = square
print(is_same(square, other_square))

gay_square = Shape('gay_square')
print(is_same(square, gay_square))

print(Shape.shape_list)


