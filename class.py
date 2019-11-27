class Point:
    x = 60
    y = 70
    def draw(self):
        print("draw")
    def move(self):
        print("move")

point1 = Point()
point1.draw()
print(point1.x)
point2 = Point()
point2.z = 10
print(point2.y, point2.z)