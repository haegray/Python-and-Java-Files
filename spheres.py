from math import *

class Sphere:

    def __init__(self,r):
        self.radius = r

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        r=self.radius
        self.area= 4 * 3.14 * (r*r)
        return (self.area)

    def getVolume(self):
        r = self.radius
        self.volume = ((4/3) * 3.14 * (r*r*r))
        return (self.volume)

def main():
    r= float(input("Enter radius:"))
    s = Sphere(r)

    print("The surface area of the sphere is:", s.surfaceArea())
    print("The volume of the sphere is: ", s.getVolume())

    if __name__ == '__main__':
        main()
