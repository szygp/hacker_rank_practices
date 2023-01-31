import math

class Points(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        sub_x = self.x - no.x
        sub_y = self.y - no.y
        sub_z = self.z - no.z
        return Points(sub_x, sub_y, sub_z)

    def dot(self, no):
        dot_product = self.x * no.x + self.y * no.y + self.z * no.z
        return dot_product

    def cross(self, no):
        cx = self.y * no.z - self.z * no.y
        cy = self.z * no.x - self.x * no.z
        cz = self.x * no.y - self.y * no.x
        return Points(cx, cy, cz)

    def absolute(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

if __name__ =='__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    # *是解压缩的意思，用于List或tuple中的元素
    x = (b-a).cross(c-b)
    #调用对象的function
    y = (c-b).cross(d-c)
    angle = math.acos(x.dot(y)/(x.absolute()*y.absolute()))
    print('%.2f' % math.degrees(angle))



